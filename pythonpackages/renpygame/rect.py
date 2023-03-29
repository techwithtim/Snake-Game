from ctypes.wintypes import DOUBLE
from typing import Optional

from pygame_sdl2.rect import *
import pygame_sdl2 as pygame
from pythonpackages.utility import flatten
import renpy.exports as renpy


class Rect(renpy.Displayable, pygame.rect.Rect):
    """https://github.com/renpy/pygame_sdl2/blob/364d3bcfa005b0eaf897d38b336a97fa6e05e76b/src/pygame_sdl2/rect.pyx#L28"""

    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        width: int = 0,
        height: int = 0,
        **kwargs
    ):

        # renpy.Displayable init
        super(Rect, self).__init__(**kwargs)

        # pygame.rect.Rect init
        super().__init__(
            left,
            top,
            width,
            height,
        )

        # The child.
        self.image: Optional[renpy.Displayable] = None

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
