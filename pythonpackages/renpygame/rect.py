from ctypes.wintypes import DOUBLE
from typing import Optional
from pythonpackages.renpygame.renpygameCDD import Render

import renpy.exports as renpy
from pygame_sdl2.rect import *

import pythonpackages.renpygame.pygame as pygame


class Rect(Render):
    """pygame: https://www.pygame.org/docs/ref/rect.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/rect.pyx#L28"""

    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        width: int = 0,
        height: int = 0,
    ):

        # Render init
        Render.__init__(self, width, height)

        # pygame.rect.Rect init
        self.internal_rect = pygame.rect.Rect.__init__(
            self, left, top, width, height)

    @property
    def left(self):
        return super().left

    @property
    def top(self):
        return super().top

    @property
    def width(self):
        return super().width

    @property
    def height(self):
        return super().height

    @property
    def right(self):
        return super().right

    @property
    def bottom(self):
        return super().bottom

    @property
    def size(self):
        return super().size

    @property
    def topleft(self):
        return super().topleft

    @property
    def topright(self):
        return super().topright

    @property
    def bottomright(self):
        return super().bottomright

    @property
    def bottomleft(self):
        return super().bottomleft

    @property
    def centerx(self):
        return super().centerx

    @property
    def centery(self):
        return super().centery

    @property
    def center(self):
        return super().center

    @property
    def midtop(self):
        return super().midtop

    @property
    def midleft(self):
        return super().midleft

    @property
    def midbottom(self):
        return super().midbottom

    @property
    def midright(self):
        return super().midright

    def copy(self):
        return self.internal_rect.copy()

    def move(self, *args):
        return self.internal_rect.move(*args)

    def move_ip(self, *args):
        return self.internal_rect.move_ip(*args)

    def inflate(self, *args):
        return self.internal_rect.inflate(*args)

    def inflate_ip(self, *args):
        return self.internal_rect.inflate_ip(*args)

    def clamp(self, other):
        return self.internal_rect.clamp(other)

    def clamp_ip(self, other):
        return self.internal_rect.clamp_ip(other)

    def clip(self, other, y=None, w=None, h=None):
        return self.internal_rect.clip(other, y, w, h)

    def union(self, other):
        return self.internal_rect.union(other)

    def union_ip(self, other):
        return self.internal_rect.union_ip(other)

    def unionall(self, other_seq):
        return self.internal_rect.unionall(other_seq)

    def unionall_ip(self, other_seq):
        return self.internal_rect.unionall_ip(other_seq)

    def fit(self, other):
        return self.internal_rect.fit(other)

    def normalize(self):
        return self.internal_rect.normalize()

    def contains(self, other):
        return self.internal_rect.contains(other)

    def collidepoint(self, x, y=None):
        return self.internal_rect.collidepoint(x, y)

    def colliderect(self, other):
        return self.internal_rect.colliderect(other)

    def collidelist(self, other_list):
        return self.internal_rect.collidelist(other_list)

    def collidelistall(self, other_list):
        return self.internal_rect.collidelistall(other_list)

    def collidedict(self, other_dict, rects_values=0):
        return self.internal_rect.collidedict(other_dict, rects_values)

    def collidedictall(self, other_dict, rects_values=0):
        return self.internal_rect.collidedictall(other_dict, rects_values)

    # my methods

    @property
    def internal_rect(self) -> pygame.rect.Rect:
        return self._internal_rect

    @internal_rect.setter
    def internal_rect(self, value: pygame.rect.Rect):
        self._internal_rect = value
