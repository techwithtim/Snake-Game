from typing import Any, Callable, Optional

import renpy.exports as renpy

import pythonpackages.renpygame as pygame
from pythonpackages.renpygame.event import EventType
from pythonpackages.renpygame.renpygameRender import Render

# https://www.renpy.org/doc/html/cdd.html


def main_render(
    child_render: Optional[Render], width: int, height: int
) -> renpy.Render:
    """is a Render that contains the child_render.
    # TODO: try to remove and return child_render
    """
    render = renpy.Render(width, height)
    if child_render:
        render.blit(child_render, child_render.get_size())
    return render


class RenpyGameByEvent(renpy.Displayable):
    """CDD: https://www.renpy.org/doc/html/cdd.html
    renpy.Displayable: https://github.com/renpy/renpy/blob/master/renpy/display/core.py#L292
    """

    def __init__(
        self,
        render_lambda: Callable[[int, int, float, float], Render],
        event_lambda: Callable[[EventType, int, int, float], Any],
        **kwargs,
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
        pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx
        """
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


def render_free_memory():
    """
    Frees memory used by the render system.
    """

    # global screen_render
    # screen_render = None

    # renpy.display.render.mark_sweep()

    renpy.display.render.render_cache.clear()

    # This can hang onto a render.
    renpy.display.interface.surftree = None


def kill_textures():
    """
    Kills all textures that have been loaded.
    """

    if renpy.display.draw is not None:
        renpy.display.draw.kill_textures()

    renpy.display.im.cache.clear()
    render_free_memory()
    renpy.text.text.layout_cache_clear()
    renpy.display.video.texture.clear()


def free_memory():
    """https://github.com/renpy/renpy/blob/ed471a56cbe82d58d8b68faf807e4f0ff860f1a5/renpy/exports.py#LL2692C1-L2705C1"""
    renpy.force_full_redraw()
    kill_textures()
    renpy.display.interface.kill_surfaces()
    renpy.text.font.free_memory()

    renpy.gc.collect(2)

    if renpy.gc.garbage:
        del renpy.gc.garbage[:]
    return


class RenpyGameByTimer(renpy.Displayable):
    """inspired by: DynamicDisplayable: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1418
    wiki: https://www.renpy.org/doc/html/displayables.html?highlight=dynamic#DynamicDisplayable
    """

    def __init__(
        self,
        first_step: Callable[[int, int, float, float], Render],
        update_process: Callable[
            [Render, float, float, Optional[float], int], Optional[float]
        ],
        event_lambda: Optional[Callable[[EventType, int, int, float], Any]] = None,
        delay: float = 0.05,
        end_game_frame: Optional[
            Callable[[Render, float, float, Optional[float], int], None]
        ] = None,
        **kwargs,
    ):
        self.first_step = first_step
        self.delay = None
        self.start_delay = delay
        self.update_process = update_process
        self.event_lambda = event_lambda
        self.child_render = None
        self.current_frame_number = 0
        self.is_started = False
        self.is_game_end = False
        self.end_game_frame = end_game_frame
        self.is_game_end_menu = False

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
    def delay(self) -> Optional[float]:
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#delay"""
        return self._delay

    @delay.setter
    def delay(self, value: Optional[float]):
        self._delay = value

    @property
    def start_delay(self) -> float:
        """start_delay is a time between frames"""
        return self._start_delay

    @start_delay.setter
    def start_delay(self, value: float):
        self._start_delay = value

    @property
    def update_process(
        self,
    ) -> Callable[[Render, float, float, Optional[float], int], Optional[float]]:
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#first_step-and-update_process"""
        return self._update_process

    @update_process.setter
    def update_process(
        self,
        value: Callable[[Render, float, float, Optional[float], int], Optional[float]],
    ):
        self._update_process = value

    @property
    def first_step(self) -> Callable[[int, int, float, float], Render]:
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#first_step-and-update_process"""
        return self._first_step

    @first_step.setter
    def first_step(self, value: Callable[[int, int, float, float], Render]):
        self._first_step = value

    @property
    def event_lambda(self) -> Optional[Callable[[Any, int, int, float], Any]]:
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#event-handling"""
        return self._event_lambda

    @event_lambda.setter
    def event_lambda(self, value: Optional[Callable[[Any, int, int, float], Any]]):
        self._event_lambda = value

    @property
    def is_game_end(self) -> bool:
        return self._is_game_end

    @is_game_end.setter
    def is_game_end(self, value: bool):
        self._is_game_end = value

    @property
    def is_game_end_menu(self) -> bool:
        return self._is_game_end_menu

    @is_game_end_menu.setter
    def is_game_end_menu(self, value: bool):
        self._is_game_end_menu = value

    @property
    def end_game_frame(
        self,
    ) -> Optional[Callable[[Render, float, float, Optional[float], int], None]]:
        """wiki:"""
        return self._end_game_frame

    @end_game_frame.setter
    def end_game_frame(
        self,
        value: Optional[Callable[[Render, float, float, Optional[float], int], None]],
    ):
        self._end_game_frame = value

    def show(self, show_and_start: bool = True):
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#start-a-game-between-a-sterted-menu"""
        print("Renpy Game Show")
        if show_and_start:
            self.start()
        renpy.call_screen("renpygame_surface", surface=self)
        return

    def start(self):
        """wiki: https://github.com/DRincs-Productions/Renpygame/wiki/Minigame-with-a-render-loop#start-a-game-between-a-sterted-menu"""
        if not self.is_started:
            print("Renpy Game Start")
            self.is_started = True
            self.delay = self.start_delay
            self._start_redraw_timer()
        else:
            print("Renpy Game Already Started")
        return

    def reset_game(self):
        print("Renpy Game Reset")
        self.delay = self.start_delay
        self.child_render = None

    def _start_redraw_timer(
        self, delay: Optional[float] = None, check_game_end: bool = True
    ):
        """inspired by: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1503"""
        if delay is None:
            delay = self.delay
        if self.delay is not None:
            renpy.redraw(self, delay)
        elif check_game_end:
            self.game_end()

    def game_end(self):
        print("Renpy Game End")
        if self.end_game_frame is not None:
            self.is_game_end_menu = True
            renpy.redraw(self, 0)
        else:
            self.quit()
        return

    def quit(self):
        self.is_game_end = True

    def render(self, width: int, height: int, st: float, at: float) -> renpy.Render:
        """this function will be started in the form of a loop.
        through start_redraw_timer, I trigger the event direnpy.redraw to create the loop.

        inspired by: https://github.com/renpy/renpy/blob/master/renpy/display/layout.py#L1534
        """

        if self.is_game_end_menu:
            self.end_game_frame(
                self.child_render, 0, 0, self.delay, self.current_frame_number
            )

        if self.current_frame_number % 3600 == 0:
            free_memory()

        # * start the timer immediately at the beginning of the function. so that update_process does not affect the fps.
        # * I don't know if this is a good idea because if update_process time > delay, the game will be looped or the game skip a frame.
        self._start_redraw_timer(check_game_end=self.current_frame_number > 0)

        if self.child_render is None:  # * first round
            self.child_render = self.first_step(width, height, st, at)
            self.current_frame_number = 0
        else:
            self.current_frame_number += 1
        # * first round and subsequent rounds
        self.delay = self.update_process(
            self.child_render, st, at, self.delay, self.current_frame_number
        )
        return main_render(self.child_render, width, height)

    def event(self, ev: EventType, x: int, y: int, st: float):
        """pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx
        config.keymap: https://www.renpy.org/doc/html/config.html#var-config.keymap
        add a event: https://www.renpy.org/doc/html/other.html#renpy.queue_event
        """
        if self.is_game_end:
            renpy.free_memory()
            return 0

        if hasattr(ev.dict, "key"):
            ev.key = None

        if pygame.WINDOWEVENT == ev.type:
            self._start_redraw_timer(check_game_end=False)
        if 32768 == ev.type:  # 32768 is the event type for pause menu
            self.reset_game()
        if self.event_lambda is not None:
            return self.event_lambda(ev, x, y, st)
