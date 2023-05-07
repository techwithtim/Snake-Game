from typing import Union

import renpy.exports as renpy

from pythonpackages.renpygame_pygame.transform import *
from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame.image import Flip, Image, Rotozoom, Scale

# https://www.renpy.org/doc/html/displayables.html


def print_error(surface, log_text) -> None:
    if isinstance(surface, Surface):
        print(
            f"{log_text}: You have passed a Surface, not an Image. probably you have to use Image.convert() first"
        )
    else:
        print(
            f"{log_text}: You have passed an invalid type: {type(surface)} or not implemented yet"
        )
    return


def flip(surface: Image, flip_x: Union[int, bool], flip_y: Union[int, bool]) -> Image:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip"""
    if isinstance(flip_x, int):
        flip_x = flip_x != 0
    if isinstance(flip_y, int):
        flip_y = flip_y != 0
    if isinstance(surface, Image):
        surface = Flip(surface, flip_x, flip_y)
    else:
        print_error(surface, "renpygame.transform.flip")
    return surface


def scale(surface: Image, size: tuple[int, int], dest_surface=None) -> Image:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale"""
    if isinstance(surface, Image):
        surface = Scale(surface, size[0], size[1])
    else:
        print_error(surface, "renpygame.transform.scale")
    return surface


def scale_by(surface, factor, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale_by"""
    print("renpygame.transform.scale_by: not implemented yet")
    # TODO: implement
    return surface


def rotate(surface, angle) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate"""
    print("renpygame.transform.rotate: not implemented yet")
    # TODO: implement
    return surface


def rotozoom(surface, angle, scale) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotozoom"""
    if isinstance(surface, Image):
        surface = Rotozoom(surface, angle, scale)
    else:
        print_error(surface, "renpygame.transform.rotozoom")
    return surface


def scale2x(surface, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale2x"""
    print("renpygame.transform.scale2x: not implemented yet")
    # TODO: implement
    return surface


def ssmoothscale(surface, size, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale"""
    print("renpygame.transform.smoothscale: not implemented yet")
    # TODO: implement
    return surface


def smoothscale_by(surface, factor, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale"""
    print("renpygame.transform.smoothscale_by: not implemented yet")
    # TODO: implement
    return surface


def chop(surface, rect) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.chop"""
    print("renpygame.transform.chop: not implemented yet")
    # TODO: implement
    return surface


def laplacian(surface, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.laplacian"""
    print("renpygame.transform.laplacian: not implemented yet")
    # TODO: implement
    return surface


def average_surfaces(surfaces, dest_surface=None, palette_colors=1) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.average_surfaces"""
    print("renpygame.transform.average_surfaces: not implemented yet")
    # TODO: implement
    return surfaces


def grayscale(surface, dest_surface=None) -> Surface:
    """pygame: https://www.pygame.org/docs/ref/transform.html#pygame.transform.grayscale
    renpy: https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L1792"""
    if isinstance(surface, Image):
        surface = renpy.display.im.Grayscale(surface)
    else:
        print_error(surface, "renpygame.transform.grayscale")
    return surface
