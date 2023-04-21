import renpy.exports as renpy
from pygame_sdl2.image import *

import pythonpackages.renpygame.pygame as pygame
from pythonpackages.renpygame.display import Surface
from pythonpackages.utility import os_path_join


class Image():
    """renpy.Image: https://github.com/renpy/renpy/blob/fb803ea05cca1b933f18d51fb0398d9545879af9/renpy/display/core.py#L292
    renpy.Image: https://github.com/renpy/renpy/blob/fb803ea05cca1b933f18d51fb0398d9545879af9/renpy/ast.py#L1198"""

    def __init__(
        self,
        path: str,
    ):
        self.path = path
        self._update()

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        self._path = value

    @property
    def displayable(self) -> renpy.Displayable:
        return self._displayable

    @displayable.setter
    def displayable(self, value: renpy.Displayable) -> None:
        self._displayable = value

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
        path = os_path_join('images', self.path)
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)
        image = image.convert()
        return image

    def _update(self) -> None:
        self.displayable = renpy.displayable(self.path)
        return

    def convert(self, width: int, height: int, st: float, at: float) -> Surface:
        surface = Surface(self.size)
        render = renpy.render(self.displayable, width, height, st, at)
        # * render.blit(self.pygame_image: used only for pygame rendering
        surface.blit(self.pygame_image, (0, 0))
        # TODO: try to remove this line and convert to renpy.Render to Surface
        surface.blit(render, (0, 0))
        return surface


def load(path: str) -> Image:
    """https://www.pygame.org/docs/ref/image.html#pygame.image.load"""
    return Image(path)
