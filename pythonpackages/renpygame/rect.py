from ctypes.wintypes import DOUBLE
from typing import Optional
from pygame_sdl2.rect import *
import renpy.exports as renpy


class Rect(renpy.Displayable):
    """https://github.com/renpy/pygame_sdl2/blob/364d3bcfa005b0eaf897d38b336a97fa6e05e76b/src/pygame_sdl2/rect.pyx#L28"""

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

        self.x = left
        self.y = top
        self.w = width
        self.h = height

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

    @property
    def left(self):
        return self.x

    @left.setter
    def left(self, value):
        self.x = value

    @property
    def top(self):
        return self.y

    @top.setter
    def top(self, value):
        self.y = value

    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, value):
        self.w = value

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, value):
        self.h = value

    @property
    def right(self):
        return self.x + self.width

    @right.setter
    def right(self, value):
        self.x += value - self.right

    @property
    def bottom(self):
        return self.y + self.height

    @bottom.setter
    def bottom(self, value):
        self.y += value - self.bottom

    @property
    def size(self):
        return (self.w, self.h)

    @size.setter
    def size(self, value):
        self.w, self.h = value

    @property
    def topleft(self):
        return (self.left, self.top)

    @topleft.setter
    def topleft(self, value):
        self.left, self.top = value

    @property
    def topright(self):
        return (self.right, self.top)

    @topright.setter
    def topright(self, value):
        self.right, self.top = value

    @property
    def bottomright(self):
        return (self.right, self.bottom)

    @bottomright.setter
    def bottomright(self, value):
        self.right, self.bottom = value

    @property
    def bottomleft(self):
        return (self.left, self.bottom)

    @bottomleft.setter
    def bottomleft(self, value):
        self.left, self.bottom = value

    @property
    def centerx(self):
        return self.x + (self.w / 2)

    @centerx.setter
    def centerx(self, value):
        self.x += value - self.centerx

    @property
    def centery(self):
        return self.y + (self.h / 2)

    @centery.setter
    def centery(self, value):
        self.y += value - self.centery

    @property
    def center(self):
        return (self.centerx, self.centery)

    @center.setter
    def center(self, value):
        self.centerx, self.centery = value

    @property
    def midtop(self):
        return (self.centerx, self.top)

    @midtop.setter
    def midtop(self, value):
        self.centerx, self.top = value

    @property
    def midleft(self):
        return (self.left, self.centery)

    @midleft.setter
    def midleft(self, value):
        self.left, self.centery = value

    @property
    def midbottom(self):
        return (self.centerx, self.bottom)

    @midbottom.setter
    def midbottom(self, value):
        self.centerx, self.bottom = value

    @property
    def midright(self):
        return (self.right, self.centery)

    @midright.setter
    def midright(self, value):
        self.right, self.centery = value
