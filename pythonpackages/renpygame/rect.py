from ctypes.wintypes import DOUBLE
from typing import Optional
from pygame_sdl2.rect import *
import renpy.exports as renpy


class Rect(renpy.Displayable):

    def __init__(
        self,
        left: int,
        top: int,
        width: int,
        height: int,
        **kwargs
    ):

        # Pass additional properties on to the renpy.Displayable
        # constructor.
        super(Rect, self).__init__(**kwargs)

        # The child.
        self.image: Optional[renpy.Displayable] = None

        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.size = (width, height)

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
