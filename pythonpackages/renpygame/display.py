from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame


class Surface():
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


class MainSurface():
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


def mode_ok(size, flags=0, depth=0, display=0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return 0


def set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> MainSurface:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    return MainSurface(size, flags, depth)


def set_icon(Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    pygame.display.set_icon(Surface)
    return


def flip():
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return


def update(rectangle=None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return


def update(rectangle_list) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return
