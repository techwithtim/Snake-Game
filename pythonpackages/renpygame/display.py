from typing import Optional
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame
from pythonpackages.renpygame.rect import Rect


class Surface():
    """https://www.pygame.org/docs/ref/surface.html"""

    def __init__(
            self,
            size: tuple[int, int] = (0, 0),
            flags: int = 0,
            depth: int = 0,
            masks=None
    ):

        self.size = size
        self.dest = None

    def blit(
            self,
            dest,
            area: Optional[tuple[int, int]] = None,
            special_flags: int = 0
    ) -> Rect:
        self.dest = dest
        return


class MainSurface(Surface):
    """https://www.pygame.org/docs/ref/surface.html"""

    def __init__(
            self,
            size=(0, 0),
            flags=0,
            depth=0,
            masks=None
    ):

        self.size = size
        self.dest = None

    def blit(
            self,
            dest,
            area=None,
            special_flags=0
    ):
        self.dest = dest
        return


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.mode_ok(size, flags, depth, display)


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> MainSurface:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    return MainSurface(size, flags, depth)


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
