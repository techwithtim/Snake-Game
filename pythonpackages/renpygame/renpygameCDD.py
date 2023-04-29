from typing import Callable, Optional

import renpy.exports as renpy

from pythonpackages.renpygame.image import get_temporary_images_render
from pythonpackages.renpygame.renpygameRender import Render

# https://www.renpy.org/doc/html/cdd.html


def main_render(child_render: Optional[Render], width: int, height: int) -> renpy.Render:
    """is a Render that contains the child_render.
    # TODO: try to remove and return child_render
    """
    render = renpy.Render(width, height)
    if child_render:
        render.blit(child_render, child_render.get_size())
    return render


class RenpyGameByEvent(renpy.Displayable):
    """CDD: https://www.renpy.org/doc/html/cdd.html
    renpy.Displayable: https://github.com/renpy/renpy/blob/master/renpy/display/core.py#L292"""

    def __init__(
        self,
            render_lambda: Callable[[int, int, float, float], Render],
            **kwargs
    ):
        # renpy.Displayable init
        super(RenpyGameByEvent, self).__init__(**kwargs)

        self.render_lambda = render_lambda
        self.child_render = None

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L170"""
        # if is first time rendering
        print("rendering RenpyGameDisplayable")
        if self.child_render is None:
            self.child_render = self.render_lambda(width, height, st, at)
        return main_render(self.child_render, width, height)

    @property
    def render_lambda(self) -> Callable[[int, int, float, float], Render]:
        """function that returns a child_render"""
        return self._render_lambda

    @render_lambda.setter
    def render_lambda(self, value: Callable[[int, int, float, float], Render]):
        self._render_lambda = value

    @property
    def child_render(self) -> Optional[Render]:
        """child_render is a Render object"""
        return self._child_render

    @child_render.setter
    def child_render(self, value: Optional[Render]):
        self._child_render = value


class RenpyGameByTimer(renpy.Displayable):
    """DynamicDisplayable: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1418
    wiki: https://www.renpy.org/doc/html/displayables.html?highlight=dynamic#DynamicDisplayable"""

    def __init__(
        self,
        first_step: Callable[[int, int, float, float], Render],
        update_process: Callable[[float, float, Render, float], tuple[Render, Optional[float]]],
        delay: float,
        **kwargs,
    ):
        self.first_step = first_step
        self.delay = delay
        self.update_process = update_process
        self.child_render = None

        # renpy.Displayable init
        super(RenpyGameByTimer, self).__init__(**kwargs)

    @property
    def child_render(self) -> Optional[Render]:
        """child_render is a Render object"""
        return self._child_render

    @child_render.setter
    def child_render(self, value: Optional[Render]):
        self._child_render = value

    def start_redraw_timer(self):
        """https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1503"""
        if self.delay is not None:
            renpy.redraw(self, self.delay)
        else:
            print("Renpy Game End")

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1534"""
        self.start_redraw_timer()

        if self.child_render is None:
            print("Renpy Game Start")
            self.child_render = self.first_step(width, height, st, at)
            # TODO: try to remove get_temporary_images_render
            self.child_render.blit(get_temporary_images_render(), (0,0))
        self.child_render, self.delay = self.update_process(
            st, at, self.child_render, self.delay)
        return main_render(self.child_render, width, height)
