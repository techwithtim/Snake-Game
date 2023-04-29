from typing import Any, Callable, Optional

import renpy.display.layout as renpylayout
import renpy.exports as renpy

# https://www.renpy.org/doc/html/cdd.html


class Render(renpy.Render):
    """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L586"""

    def __init__(
        self,
        width: int,
        height: int,
    ):

        # renpy.Render init
        super().__init__(width, height)
        # * Render properties, will come set in super().__init__

    @property
    def mark(self):
        return super().mark

    @property
    def cache_killed(self):
        return super().cache_killed

    @property
    def killed(self):
        return super().killed

    @property
    def width(self) -> int:
        """must be int"""
        return int(super().width)

    @property
    def height(self) -> int:
        """must be int"""
        return int(super().height)

    @property
    def layer_name(self):
        return super().layer_name

    @property
    def children(self):
        return super().children

    @property
    def forward(self):
        return super().forward

    @property
    def reverse(self):
        return super().reverse

    @property
    def alpha(self):
        return super().alpha

    @property
    def over(self):
        return super().over

    @property
    def nearest(self):
        return super().nearest

    @property
    def focuses(self):
        return super().focuses

    @property
    def pass_focuses(self):
        return super().pass_focuses

    @property
    def focus_screen(self):
        return super().focus_screen

    @property
    def render_of(self):
        return super().render_of

    @property
    def xclipping(self):
        return super().xclipping

    @property
    def yclipping(self):
        return super().yclipping

    @property
    def modal(self):
        return super().modal

    @property
    def text_input(self):
        return super().text_input

    @property
    def parents(self):
        return super().parents

    @property
    def depends_on_list(self):
        return super().depends_on_list

    @property
    def operation(self):
        return super().operation

    @property
    def operation_complete(self):
        return super().operation_complete

    @property
    def operation_alpha(self):
        return super().operation_alpha

    @property
    def operation_parameter(self):
        return super().operation_parameter

    @property
    def surface(self):
        return super().surface

    @property
    def alpha_surface(self):
        return super().alpha_surface

    @property
    def half_cache(self):
        return super().half_cache

    @property
    def mesh(self):
        return super().mesh

    @property
    def shaders(self):
        return super().shaders

    @property
    def uniforms(self):
        return super().uniforms

    @property
    def properties(self):
        return super().properties

    @property
    def cached_texture(self):
        return super().cached_texture

    @property
    def cached_model(self):
        return super().cached_model

    @property
    def loaded(self):
        return super().loaded

    def blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        """render.blit(): https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L778"""
        return super().blit(source, pos, focus, main, index)

    def subpixel_blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        return super().subpixel_blit(source, pos, focus, main, index)

    def absolute_blit(self, source, pos: tuple[int, int], focus=True, main=True, index=None) -> int:
        return super().absolute_blit(source, pos, focus, main, index)

    def get_size(self) -> tuple[int, int]:
        return super().get_size()

    def render_to_texture(self, alpha=True):
        return super().render_to_texture(alpha)

    def subsurface(self, rect, focus=False):
        return super().subsurface(rect, focus)

    def depends_on(self, source, focus=False):
        return super().depends_on(source, focus)

    def kill_cache(self):
        return super().kill_cache()

    def kill(self):
        return super().kill()

    def add_focus(self, d, arg=None, x=0, y=0, w=None, h=None, mx=None, my=None, mask=None):
        return super().add_focus(d, arg, x, y, w, h, mx, my, mask)

    def take_focuses(self, cminx, cminy, cmaxx, cmaxy, transform, screen, focuses):
        return super().take_focuses(cminx, cminy, cmaxx, cmaxy, transform, screen, focuses)

    def focus_at_point(self, x, y, screen):
        return super().focus_at_point(x, y, screen)

    def main_displayables_at_point(self, x, y, layers, depth=None):
        return super().main_displayables_at_point(x, y, layers, depth)

    def is_pixel_opaque(self, x, y):
        return super().is_pixel_opaque(x, y)

    def fill(self, color):
        return super().fill(color)

    def canvas(self):
        return super().canvas()

    def screen_rect(self, sx: float, sy: float, transform: list[list[int]]):
        return super().screen_rect(sx, sy, transform)

    def place(self, d, x=0, y=0, width=None, height=None, st=None, at=None, render=None, main=True):
        return super().place(d, x, y, width, height, st, at, render, main)

    def zoom(self, xzoom, yzoom):
        return super().zoom(xzoom, yzoom)

    def add_shader(self, shader):
        return super().add_shader(shader)

    def add_uniform(self, name, value):
        return super().add_uniform(name, value)

    def add_property(self, name, value):
        return super().add_property(name, value)

    # my methods

    def get_width(self) -> int:
        width, _ = self.get_size()
        return int(width)

    def get_height(self) -> int:
        _, height = self.get_size()
        return int(height)

    def import_renpy_render(self, renpy_render: renpy.Render):
        self = renpy_render


# class Canvas(renpy.Canvas):
#     """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1610"""

#     def __init__(self, surf):

#         # renpy.Canvas init
#         super().__init__(surf)

#     def rect(self, color, rect, width=0):
#         return super().rect(color, rect, width)

#     def polygon(self, color, pointlist, width=0):
#         return super().polygon(color, pointlist, width)

#     def circle(self, color, pos, radius, width=0):
#         return super().circle(color, pos, radius, width)

#     def ellipse(self, color, rect, width=0):
#         return super().ellipse(color, rect, width)

#     def arc(self, color, rect, start_angle, stop_angle, width=1):
#         return super().arc(color, rect, start_angle, stop_angle, width)

#     def line(self, color, start_pos, end_pos, width=1):
#         return super().line(color, start_pos, end_pos, width)

#     def lines(self, color, closed, pointlist, width=1):
#         return super().lines(color, closed, pointlist, width)

#     def aaline(self, color, startpos, endpos, blend=1):
#         return super().aaline(color, startpos, endpos, blend)

#     def aalines(self, color, closed, pointlist, blend=1):
#         return super().aalines(color, closed, pointlist, blend)

#     def get_surface(self):
#         return super().get_surface()

def main_render(child_render: Optional[Render], width: int, height: int) -> renpy.Render:
    """is a Render that contains the child_render.
    # TODO: try to remove and return child_render
    """
    render = renpy.Render(width, height)
    if child_render:
        render.blit(child_render, child_render.get_size())
    return render


class RenpyGameDisplayable(renpy.Displayable):
    """CDD: https://www.renpy.org/doc/html/cdd.html
    renpy.Displayable: https://github.com/renpy/renpy/blob/master/renpy/display/core.py#L292"""

    def __init__(
        self,
            child_render: Render,
            **kwargs
    ):
        # renpy.Displayable init
        super(RenpyGameDisplayable, self).__init__(**kwargs)

        self.child_render = child_render

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L170"""
        self.child_render = self.render_lambda(width, height, st, at)
        return main_render(self.child_render, width, height)

    @property
    def child_render(self) -> Render:
        """child_render is a Render object"""
        return self._child_render

    @child_render.setter
    def child_render(self, value: Render):
        self._child_render = value


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

    def update(self, st, at):
        """https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1503"""
        self.last_st = st
        self.last_at = at

        if self.delay is not None:
            renpy.redraw(self, self.delay)
        else:
            print("Renpy Game End")

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1534"""
        self.update(st, at)

        if self.child_render is None:
            print("Renpy Game Start")
            self.child_render = self.first_step(width, height, st, at)
        self.child_render, self.delay = self.update_process(
            st, at, self.child_render, self.delay)
        return main_render(self.child_render, width, height)


# class Displayable(renpy.Displayable):
#     """https://github.com/renpy/renpy/blob/c15f4c3487be27ff1095af955c605b68396591df/renpy/display/core.py#L292"""

#     def __init__(self, focus=None, default=None, style=None, _args=None, tooltip=None, default_focus=None, **properties):
#         super().__init__(focus, default, style, _args, tooltip, default_focus, **properties)
