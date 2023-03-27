from ctypes.wintypes import DOUBLE
from typing import Optional

from more_itertools import flatten
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

    # renpy

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

    # pygame

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

    def copy(self):
        return Rect(self)

    def move(self, *args):
        r = self.copy()
        r.move_ip(*args)
        return r

    def move_ip(self, *args):
        x, y = flatten(args)
        self.x += x
        self.y += y

    def inflate(self, *args):
        r = self.copy()
        r.inflate_ip(*args)
        return r

    def inflate_ip(self, *args):
        x, y = flatten(args)
        c = self.center
        self.w += x
        self.h += y
        self.center = c

    def clamp(self, other):
        r = self.copy()
        r.clamp_ip(other)
        return r

    def clamp_ip(self, other):
        if not isinstance(other, Rect):
            other = Rect(other)

        if self.w > other.w or self.h > other.h:
            self.center = other.center
        else:
            if self.left < other.left:
                self.left = other.left
            elif self.right > other.right:
                self.right = other.right
            if self.top < other.top:
                self.top = other.top
            elif self.bottom > other.bottom:
                self.bottom = other.bottom

    def clip(self, other, y=None, w=None, h=None):
        if type(other) == int:
            other = Rect(other, y, w, h)

        if not isinstance(other, Rect):
            other = Rect(other)

        if not self.colliderect(other):
            return Rect(0, 0, 0, 0)

        r = self.copy()

        # Remember that (0,0) is the top left.
        if r.left < other.left:
            d = other.left - r.left
            r.left += d
            r.width -= d
        if r.right > other.right:
            d = r.right - other.right
            r.width -= d
        if r.top < other.top:
            d = other.top - r.top
            r.top += d
            r.height -= d
        if r.bottom > other.bottom:
            d = r.bottom - other.bottom
            r.height -= d

        return r

    def union(self, other):
        r = self.copy()
        r.union_ip(other)
        return r

    def union_ip(self, other):
        if not isinstance(other, Rect):
            other = Rect(other)

        x = min(self.x, other.x)
        y = min(self.y, other.y)
        self.w = max(self.right, other.right) - x
        self.h = max(self.bottom, other.bottom) - y
        self.x = x
        self.y = y

    def unionall(self, other_seq):
        r = self.copy()
        r.unionall_ip(other_seq)
        return r

    def unionall_ip(self, other_seq):
        for other in other_seq:
            self.union_ip(other)

    def fit(self, other):
        if not isinstance(other, Rect):
            other = Rect(other)

        # Not sure if this is entirely correct. Docs and tests are ambiguous.
        r = self.copy()
        r.topleft = other.topleft
        w_ratio = other.w / float(r.w)
        h_ratio = other.h / float(r.h)
        factor = min(w_ratio, h_ratio)
        r.w *= factor
        r.h *= factor
        return r

    def normalize(self):
        if self.w < 0:
            self.x += self.w
            self.w = -self.w
        if self.h < 0:
            self.y += self.h
            self.h = -self.h

    def contains(self, other):
        if not isinstance(other, Rect):
            other = Rect(other)

        return other.x >= self.x and other.right <= self.right and \
            other.y >= self.y and other.bottom <= self.bottom and \
            other.left < self.right and other.top < self.bottom

    def collidepoint(self, x, y=None):
        if type(x) == tuple:
            x, y = x
        return x >= self.x and y >= self.y and \
            x < self.right and y < self.bottom

    def colliderect(self, other):
        if not isinstance(other, Rect):
            other = Rect(other)

        return self.left < other.right and self.top < other.bottom and \
            self.right > other.left and self.bottom > other.top

    def collidelist(self, other_list):
        for n, other in zip(range(len(other_list)), other_list):
            if self.colliderect(other):
                return n
        return -1

    def collidelistall(self, other_list):
        ret = []
        for n, other in zip(range(len(other_list)), other_list):
            if self.colliderect(other):
                ret.append(n)
        return ret

    def collidedict(self, other_dict, rects_values=0):
        # What is rects_values supposed to do? Not in docs.
        for key, val in other_dict.items():
            if self.colliderect(val):
                return key, val
        return None

    def collidedictall(self, other_dict, rects_values=0):
        ret = []
        for key, val in other_dict.items():
            if self.colliderect(val):
                ret.append((key, val))
        return ret
