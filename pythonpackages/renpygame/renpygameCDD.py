from typing import Any, Callable, Optional
from pythonpackages.renpygame.event import EventType

import renpy.exports as renpy

import pythonpackages.renpygame as pygame
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
            event_lambda: Callable[[EventType, int, int, float], Any],
            **kwargs
    ):
        # renpy.Displayable init
        super(RenpyGameByEvent, self).__init__(**kwargs)

        self.render_lambda = render_lambda
        self.event_lambda = event_lambda
        self.child_render = None

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L170"""
        # if is first time rendering
        print("rendering RenpyGameDisplayable")
        if self.child_render is None:
            self.child_render = self.render_lambda(width, height, st, at)
        return main_render(self.child_render, width, height)

    def event(self, ev: EventType, x: int, y: int, st: float):
        """keys: https://www.pygame.org/docs/ref/key.html#key-constants-label
        pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx"""
        return self.event_lambda(ev, x, y, st)

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
    """inspired by: DynamicDisplayable: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1418
    wiki: https://www.renpy.org/doc/html/displayables.html?highlight=dynamic#DynamicDisplayable"""

    def __init__(
        self,
        first_step: Callable[[int, int, float, float], Render],
        update_process: Callable[[float, float, Render, float], Optional[float]],
        event_lambda: Optional[Callable[[
            EventType, int, int, float], Any]] = None,
        delay: float = 0.05,
        **kwargs,
    ):
        self.first_step = first_step
        self.delay = delay
        self.start_delay = delay
        self.update_process = update_process
        self.event_lambda = event_lambda
        self.child_render = None

        # renpy.Displayable init
        super(RenpyGameByTimer, self).__init__(**kwargs)

    @property
    def child_render(self) -> Optional[Render]:
        """child_render is a Render object and is a current frame of the game"""
        return self._child_render

    @child_render.setter
    def child_render(self, value: Optional[Render]):
        self._child_render = value

    @property
    def delay(self) -> float:
        """delay is a time between frames"""
        return self._delay

    @delay.setter
    def delay(self, value: float):
        self._delay = value

    @property
    def start_delay(self) -> float:
        """start_delay is a time between frames"""
        return self._start_delay

    @start_delay.setter
    def start_delay(self, value: float):
        self._start_delay = value

    @property
    def update_process(self) -> Callable[[float, float, Render, float], Optional[float]]:
        """update_process is a function that edit a child_render.
        Return a delay or None, if is None, the game will end.
        Not return a child_render for set a child_render, because it is a Object, so it is not a copy, but a reference."""
        return self._update_process

    @update_process.setter
    def update_process(self, value: Callable[[float, float, Render, float], Optional[float]]):
        self._update_process = value

    @property
    def first_step(self) -> Callable[[int, int, float, float], Render]:
        """first_step is a function that return a child_render, it is a first frame of the game"""
        return self._first_step

    @first_step.setter
    def first_step(self, value: Callable[[int, int, float, float], Render]):
        self._first_step = value

    @property
    def event_lambda(self) -> Optional[Callable[[Any, int, int, float], Any]]:
        """event_lambda is a function that return a child_render, it is a first frame of the game"""
        return self._event_lambda

    @event_lambda.setter
    def event_lambda(self, value: Optional[Callable[[Any, int, int, float], Any]]):
        self._event_lambda = value

    def reset_game(self):
        print("Renpy Game Reset")
        self.delay = self.start_delay
        self.child_render = None

    def start_redraw_timer(self, delay: Optional[float] = None, check_game_end: bool = True):
        """inspired by: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1503"""
        if (delay is None):
            delay = self.delay
        if self.delay is not None:
            renpy.redraw(self, delay)
        elif check_game_end:
            print("Renpy Game End")

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """this function will be started in the form of a loop.
        through start_redraw_timer, I trigger the event direnpy.redraw to create the loop.

        inspired by: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1534"""
        renpy.queue_event("RENPYGAME_REDRAW", up=False)

        # * start the timer immediately at the beginning of the function. so that update_process does not affect the fps.
        # * I don't know if this is a good idea because if update_process time > delay, the game will be looped or the game skip a frame.
        self.start_redraw_timer()

        if self.child_render is None:  # * first round
            print("Renpy Game Start")
            self.child_render = self.first_step(width, height, st, at)
        # * first round and subsequent rounds
        self.delay = self.update_process(
            st, at, self.child_render, self.delay)
        return main_render(self.child_render, width, height)

    def event(self, ev: EventType, x: int, y: int, st: float):
        """pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx
        config.keymap: https://www.renpy.org/doc/html/config.html#var-config.keymap
        add a event: https://www.renpy.org/doc/html/other.html#renpy.queue_event
        """
        if (pygame.WINDOWEVENT == ev.type):
            self.start_redraw_timer(check_game_end=False)
        if (32768 == ev.type):  # 32768 is the event type for pause menu
            self.reset_game()
        if self.event_lambda is not None:
            return self.event_lambda(ev, x, y, st)
