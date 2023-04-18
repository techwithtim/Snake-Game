from typing import Optional
import renpy.exports as renpy
from pygame_sdl2.image import *

import pythonpackages.renpygame.pygame as pygame


class RenpyGameImage():
    """renpy.Image: https://github.com/renpy/renpy/blob/fb803ea05cca1b933f18d51fb0398d9545879af9/renpy/display/core.py#L292
    renpy.Image: https://github.com/renpy/renpy/blob/fb803ea05cca1b933f18d51fb0398d9545879af9/renpy/ast.py#L1198"""

    def __init__(
        self,
        path: str,
    ):
        self.path = path

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value

    @property
    def displayable(self) -> renpy.Displayable:
        return renpy.displayable(self.path)

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def file(self):
        return renpy.open_file(self.path)

    @property
    def pygame_image(self) -> pygame.Surface:
        return pygame.image.load(self.file)

    def convert(self) -> renpy.Render:
        return renpy.render(self.displayable, self.width, self.height)


def load(file: str) -> Optional[RenpyGameImage]:
    """https://www.pygame.org/docs/ref/image.html#pygame.image.load"""
    displayable = renpy.displayable(file)
    return RenpyGameImage(displayable)
