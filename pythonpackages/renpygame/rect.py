from ctypes.wintypes import DOUBLE
from typing import Optional

import renpy.exports as renpy
from pygame_sdl2.rect import *

import pythonpackages.renpygame.pygame as pygame


class Rect(renpy.Displayable, pygame.rect.Rect):
    """https://www.pygame.org/docs/ref/rect.html"""

    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        width: int = 0,
        height: int = 0,
        image: Optional[str] = None,
        **kwargs
    ):

        # renpy.Displayable init
        super(Rect, self).__init__(**kwargs)

        # The width and height of us, and our child.
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.image = image

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value: str):
        if value:
            self._image = renpy.displayable(value)
        else:
            self._image = None

    def render(self, width: int, height: int, st: DOUBLE, at: DOUBLE):
        # Create the render we will return.
        render = renpy.Render(self.width, self.height)

        if self.image:
            # Create a render from the child.
            child_render = renpy.render(self.image, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (self.left, self.top))

        # Return the render.
        return render
