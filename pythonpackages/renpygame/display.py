from typing import Any, Optional, Union
from pythonpackages.renpygame.rect import Rect
import renpy.exports as renpy
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame


class Surface(renpy.Displayable, pygame.Surface):
    """https://www.pygame.org/docs/ref/surface.html"""

    def __init__(
        self,
        size: tuple[int, int] = (0, 0),
        flags: int = 0,
        depth: int = 0,
        masks=None,  # Optional[ColorValue]
        **kwargs
    ):
        # renpy.Displayable init
        super(Surface, self).__init__(**kwargs)

        # pygame.Surface init
        pygame.Surface.__init__(self, size, flags, depth, masks)

    def blit(
        self,
        source,  # Surface
        dest,
        area: Optional[tuple[int, int]] = None,
        special_flags: int = 0
    ):
        pygame.Surface.blit(self, source, dest, area, special_flags)
        return


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> Surface:
    """If it is commented out it will replace the renpy screen creating an error when returning to renpy. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    # * It has the job of replacing the original so nothing happens
    return Surface(size, flags, depth)


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)


def set_icon(Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    return pygame.display.set_icon(Surface)


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return pygame.display.flip()


def update(rectangle: Optional[Union[list, Any]] = None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return pygame.display.update(rectangle)
