from typing import Any, Optional, Union
from pythonpackages.renpygame.rect import Rect
from pythonpackages.renpygame.renpygameCDD import Render
import renpy.exports as renpy
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame


class Surface(Render):
    """pygame: https://www.pygame.org/docs/ref/surface.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/48e9c45667152a4ccf98d6d9251eeb3c8858b5f1/src/pygame_sdl2/surface.pyx#L53"""

    def __init__(
        self,
        size: tuple[int, int] = (0, 0),
        flags: int = 0,
        depth: int = 0,
        masks=None,  # Optional[ColorValue]
        **kwargs
    ):
        # Render init
        super().__init__(size[0], size[1])


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> Surface:
    """If it is commented out it will replace the renpy screen creating an error when returning to renpy. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    # * It has the job of replacing the original so nothing happens
    return Surface(size, flags, depth)


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)


def set_icon(Surface: Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    return pygame.display.set_icon(Surface)


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return pygame.display.flip()


def update(rectangle: Optional[Union[list, Any]] = None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return pygame.display.update(rectangle)
