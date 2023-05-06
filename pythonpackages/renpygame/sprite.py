import renpy.exports as renpy

import pythonpackages.renpygame_pygame as pygame
from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame.rect import Rect
from pythonpackages.renpygame_pygame.sprite import *


class Sprite(pygame.sprite.Sprite):
    """pygame: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L106
    """

    def __init__(self, *groups, **kwargs):
        # Sprite init
        super().__init__(*groups, **kwargs)

    def add(self, *groups):
        return super().add(*groups)

    def remove(self, *groups):
        return super().remove(*groups)

    def add_internal(self, group):
        return super().add_internal(group)

    def remove_internal(self, group):
        return super().remove_internal(group)

    def update(self, *args):
        return super().update(*args)

    def kill(self):
        return super().kill()

    def groups(self) -> list[AbstractGroup]:
        return super().groups()

    def alive(self) -> bool:
        return super().alive()


class AbstractGroup(pygame.sprite.AbstractGroup):
    """pygame: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L284
    pygame_sdl2:"""

    def AbstractGroup(self):
        # Sprite init
        super().__init__()

    def sprites(self) -> list[Sprite]:
        return super().sprites()

    def add_internal(self, sprite):
        return super().add_internal(sprite)

    def remove_internal(self, sprite):
        return super().remove_internal(sprite)

    def has_internal(self, sprite) -> bool:
        return super().has_internal(sprite)

    def copy(self) -> pygame.sprite.AbstractGroup:
        return super().copy()

    def add(self, *sprites):
        return super().add(*sprites)

    def remove(self, *sprites):
        return super().remove(*sprites)

    def has(self, *sprites) -> bool:
        return super().has(*sprites)

    def update(self, *args):
        return super().update(*args)

    def draw(self, surface):
        return super().draw(surface)

    def clear(self, surface: Surface, bgd):
        # * Is commented for improved performance
        # return super().clear(surface, bgd)
        surface.blit(bgd, (0, 0))
        return

    def empty(self):
        return super().empty()


class Group(pygame.sprite.Group):
    """pygame:
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L531
    """

    def __init__(self, *sprites):
        super().__init__(*sprites)

    def clear(self, surface: Surface, bgd):
        return AbstractGroup.clear(self, surface, bgd)


class RenderUpdates(pygame.sprite.RenderUpdates):
    """pygame: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L557
    """

    def draw(self, surface: Surface) -> list[Rect]:
        return super().draw(surface)

    def clear(self, surface: Surface, bgd):
        return AbstractGroup.clear(self, surface, bgd)
