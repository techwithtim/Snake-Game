import pythonpackages.renpygame_pygame as pygame
from pythonpackages.renpygame_pygame.rect import *
from pythonpackages.renpygame.renpygameRender import Render


class Rect(Render):
    """pygame: https://www.pygame.org/docs/ref/rect.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/rect.pyx#L28
    """

    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        width: int = 0,
        height: int = 0,
    ):
        # Render init
        Render.__init__(self, width, height)

        # pygame.Rect init
        self.internal_rect = pygame.Rect(left, top, width, height)

    def __reduce__(self):
        return self.internal_rect.__reduce__()

    def __repr__(self):
        return self.internal_rect.__repr__()

    def __len__(self):
        return self.internal_rect.__len__()

    def __iter__(self):
        return self.internal_rect.__iter__()

    def __richcmp__(self, a, b, op: int):
        return self.internal_rect.__richcmp__(a, b, op)

    def __getitem__(self, key):
        return self.internal_rect.__getitem__(key)

    def __setitem__(self, key, val):
        return self.internal_rect.__setitem__(key, val)

    @property
    def left(self) -> int:
        return self.internal_rect.left

    @left.setter
    def left(self, value: int):
        self.internal_rect.left = value

    @property
    def top(self) -> int:
        return self.internal_rect.top

    @top.setter
    def top(self, value: int):
        self.internal_rect.top = value

    # * they are already defined in Render
    # @property
    # def width(self) -> int:
    #     return int(super().width)

    # @width.setter
    # def width(self, value):
    #     super().width = value

    # @property
    # def height(self) -> int:
    #     return int(super().height)

    # @height.setter
    # def height(self, value):
    #     super().height = value

    @property
    def right(self):
        return self.internal_rect.right

    @right.setter
    def right(self, value):
        self.internal_rect.right = value

    @property
    def bottom(self):
        return self.internal_rect.bottom

    @bottom.setter
    def bottom(self, value):
        self.internal_rect.bottom = value

    @property
    def size(self):
        return self.internal_rect.size

    @size.setter
    def size(self, value):
        self.internal_rect.size = value

    @property
    def topleft(self):
        return self.internal_rect.topleft

    @topleft.setter
    def topleft(self, value):
        self.internal_rect.topleft = value

    @property
    def topright(self):
        return self.internal_rect.topright

    @topright.setter
    def topright(self, value):
        self.internal_rect.topright = value

    @property
    def bottomright(self):
        return self.internal_rect.bottomright

    @bottomright.setter
    def bottomright(self, value):
        self.internal_rect.bottomright = value

    @property
    def bottomleft(self):
        return self.internal_rect.bottomleft

    @bottomleft.setter
    def bottomleft(self, value):
        self.internal_rect.bottomleft = value

    @property
    def centerx(self):
        return self.internal_rect.centerx

    @centerx.setter
    def centerx(self, value):
        self.internal_rect.centerx = value

    @property
    def centery(self):
        return self.internal_rect.centery

    @centery.setter
    def centery(self, value):
        self.internal_rect.centery = value

    @property
    def center(self):
        return self.internal_rect.center

    @center.setter
    def center(self, value):
        self.internal_rect.center = value

    @property
    def midtop(self):
        return self.internal_rect.midtop

    @midtop.setter
    def midtop(self, value):
        self.internal_rect.midtop = value

    @property
    def midleft(self):
        return self.internal_rect.midleft

    @midleft.setter
    def midleft(self, value):
        self.internal_rect.midleft = value

    @property
    def midbottom(self):
        return self.internal_rect.midbottom

    @midbottom.setter
    def midbottom(self, value):
        self.internal_rect.midbottom = value

    @property
    def midright(self):
        return self.internal_rect.midright

    @midright.setter
    def midright(self, value):
        self.internal_rect.midright = value

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
    def internal_rect(self) -> pygame.Rect:
        return self._internal_rect

    @internal_rect.setter
    def internal_rect(self, value: pygame.Rect):
        self._internal_rect = value
