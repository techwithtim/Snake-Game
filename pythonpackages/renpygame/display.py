from typing import Any, Optional, Union

import renpy.exports as renpy

import pythonpackages.renpygame_pygame as pygame
from pythonpackages.renpygame_pygame.display import *
from pythonpackages.renpygame.rect import Rect
from pythonpackages.renpygame.renpygameRender import Render


class Surface(Render):
    """pygame: https://www.pygame.org/docs/ref/surface.html
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/surface.pyx#L53
    """

    def __init__(
        self,
        size: tuple[int, int] = (0, 0),
        flags: int = 0,
        depth: int = 0,
        masks=None,  # Optional[ColorValue]
    ):
        # Render init
        # super().__init__(size[0], size[1])
        Render.__init__(self, size[0], size[1])

        # pygame.Surface init
        self.internal_surface = pygame.Surface(size, flags, depth, masks)

    def blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> Rect:
        """pygame: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/surface.pyx#L182
        """
        if isinstance(source, pygame.Surface):
            self.internal_surface.blit(source, pos)
        if isinstance(pos, Rect) or isinstance(pos, pygame.Rect):
            pos = (pos.left, pos.top)
        super().blit(source, pos, focus, main, index)
        if isinstance(source, Surface) or isinstance(source, pygame.Surface):
            return source.get_rect()
        elif isinstance(source, Rect) or isinstance(source, pygame.Rect):
            return source
        elif isinstance(source, renpy.Render):
            return Rect()
        else:
            raise TypeError(
                f"renpygame.display.Surface.blit(): you have passed an invalid type: {type(source)} or not implemented yet"
            )

    def convert(self, surface=None):
        return self.internal_surface.convert(surface)

    def convert_alpha(self, surface=None):
        return self.internal_surface.convert_alpha(surface)

    def copy(self):
        return self.internal_surface.copy()

    def fill(self, color, rect=None, special_flags=0):
        self.internal_surface.fill(color, rect, special_flags)
        return super().fill(color)

    def scroll(self, dx: int = 0, dy: int = 0):
        return self.internal_surface.scroll(dx, dy)

    def set_colorkey(self, color, flags=0):
        return self.internal_surface.set_colorkey(color, flags)

    def get_colorkey(self):
        return self.internal_surface.get_colorkey()

    def set_alpha(self, value, flags=0):
        return self.internal_surface.set_alpha(value, flags)

    def get_alpha(self):
        return self.internal_surface.get_alpha()

    def lock(self, lock=None):
        return self.internal_surface.lock(lock)

    def unlock(self, lock=None):
        return self.internal_surface.unlock(lock)

    def mustlock(self):
        return self.internal_surface.mustlock()

    def get_locked(self):
        return self.internal_surface.get_locked()

    def get_locks(self):
        return self.internal_surface.get_locks()

    def get_at(self, pos):
        return self.internal_surface.get_at(pos)

    def set_at(self, pos, color):
        return self.internal_surface.set_at(pos, color)

    def get_at_mapped(self, pos):
        return self.internal_surface.get_at_mapped(pos)

    def map_rgb(self, color):
        return self.internal_surface.map_rgb(color)

    def unmap_rgb(self, pixel):
        return self.internal_surface.unmap_rgb(pixel)

    def set_clip(self, rect):
        return self.internal_surface.set_clip(rect)

    def get_clip(self):
        return self.internal_surface.get_clip()

    def subsurface(self, *args):
        self.internal_surface.subsurface(*args)
        return super().subsurface(*args)

    def get_parent(self):
        return self.internal_surface.get_parent()

    def get_abs_parent(self):
        return self.internal_surface.get_abs_parent()

    def get_offset(self):
        return self.internal_surface.get_offset()

    def get_abs_offset(self):
        return self.internal_surface.get_abs_offset()

    def get_size(self):
        self.internal_surface.get_size()
        return super().get_size()

    def get_width(self):
        self.internal_surface.get_width()
        return super().get_width()

    def get_height(self):
        self.internal_surface.get_height()
        return super().get_height()

    def get_rect(self, **kwargs) -> Rect:
        """https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/surface.pyx#L710"""
        rv = Rect(0, 0, self.width, self.height)

        for k, v in kwargs.items():
            setattr(rv, k, v)

        # rv.renpygame_render = self.renpygame_render

        return rv

    def get_bitsize(self):
        return self.internal_surface.get_bitsize()

    def get_bytesize(self):
        return self.internal_surface.get_bytesize()

    def get_flags(self):
        return self.internal_surface.get_flags()

    def get_pitch(self):
        return self.internal_surface.get_pitch()

    def get_masks(self):
        return self.internal_surface.get_masks()

    def set_masks(self, masks):
        return self.internal_surface.set_masks(masks)

    def get_shifts(self):
        return self.internal_surface.get_shifts()

    def set_shifts(self, shifts):
        return self.internal_surface.set_shifts(shifts)

    def get_losses(self):
        return self.internal_surface.get_losses()

    def get_bounding_rect(self, min_alpha=1):
        return self.internal_surface.get_bounding_rect(min_alpha)

    def get_view(self, kind="2"):
        return self.internal_surface.get_view(kind)

    def get_buffer(self):
        return self.internal_surface.get_buffer()

    def from_data(self, data):
        return self.internal_surface.from_data(data)

    # my methods

    @property
    def internal_surface(self) -> pygame.Surface:
        return self._internal_surface

    @internal_surface.setter
    def internal_surface(self, value: pygame.Surface):
        self._internal_surface = value


def set_mode(
    size: tuple[int, int] = (0, 0),
    flags: int = 0,
    depth: int = 0,
    display: int = 0,
    vsync: int = 0,
) -> Surface:
    """If it is commented out it will replace the renpy screen creating an error when returning to renpy. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    # * It has the job of replacing the original so nothing happens
    return Surface(size, flags, depth)


def mode_ok(
    size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0
) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)  # type: ignore


def set_icon(Surface: pygame.Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    if not isinstance(Surface, pygame.Surface):
        print(
            "set_icon(): Warning: Surface is not a pygame_sdl2.surface.Surface, it is a",
            type(Surface),
        )
        print("if you have a renpyGame Image you can use image.pygame_image")
    return pygame.display.set_icon(Surface)  # type: ignore


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return pygame.display.flip()  # type: ignore


def update(rectangle: Optional[Union[list, Any]] = None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return pygame.display.update(rectangle)  # type: ignore
