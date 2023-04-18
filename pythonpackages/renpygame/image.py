import renpy.exports as renpy
from pygame_sdl2.image import *

import pythonpackages.renpygame.pygame as pygame


class RenpyGameImage(renpy.Render):
    """pygame: https://www.pygame.org/docs/ref/surface.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/48e9c45667152a4ccf98d6d9251eeb3c8858b5f1/src/pygame_sdl2/surface.pyx#L53"""

    def __init__(
        self,
        displayable: renpy.Displayable,
    ):
        self.displayable = displayable

    @property
    def displayable(self) -> renpy.Displayable:
        return self._displayable

    @displayable.setter
    def displayable(self, value: renpy.Displayable) -> None:
        self._displayable = value
        self._width, self._height = self.displayable.get_size()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def convert(self):
        return renpy.render(self.displayable, self.width, self.height)


def load(file: str) -> RenpyGameImage:
    """https://www.pygame.org/docs/ref/image.html#pygame.image.load"""
    if isinstance(file, str):
        displayable = renpy.displayable(file)
        return RenpyGameImage(displayable)
