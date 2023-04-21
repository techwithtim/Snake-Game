from typing import Union
from pygame_sdl2.transform import *

from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame.image import Flip, Image
import renpy.exports as renpy

# https://www.renpy.org/doc/html/displayables.html


def flip(surface: Image, flip_x: Union[int, bool], flip_y: Union[int, bool]) -> Image:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip"""
    if isinstance(flip_x, int):
        flip_x = flip_x != 0
    if isinstance(flip_y, int):
        flip_y = flip_y != 0
    if isinstance(surface, Image):
        surface = Flip(surface, flip_x, flip_y)
    elif isinstance(surface, Surface):
        raise TypeError(
            "renpygame.transform.flip: You have passed a Surface, not an Image. probably you have to use Image.convert() first")
    else:
        raise TypeError(
            "renpygame.transform.flip: You have passed an invalid type or not implemented yet")
    return surface


def scale(surface: Image, size: tuple[int, int], dest_surface=None) -> Image:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale"""
    # TODO: implement
    return surface
