from typing import Optional

import renpy.exports as renpy
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame
from pythonpackages.renpygame.rect import Rect


class Surface(renpy.Displayable, pygame.Surface):
    """https://www.pygame.org/docs/ref/surface.html"""

    def __init__(
        self,
        size: tuple[int, int] = (0, 0),
        flags: int = 0,
        depth: int = 0,
        masks=None,
        **kwargs
    ):
        # renpy.Displayable init
        super(Surface, self).__init__(**kwargs)

        self.size = size
        self.dest = None


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> MainSurface:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    return Surface(size, flags, depth)


def set_icon(Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    return pygame.display.set_icon(Surface)


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return


def update(rectangle=None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return


def update(rectangle_list) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return
