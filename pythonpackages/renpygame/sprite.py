from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame.renpygameCDD import Render
import renpy.exports as renpy
from pygame_sdl2.sprite import *

import pythonpackages.renpygame.pygame as pygame


class Sprite(pygame.sprite.Sprite):
    """pygame: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L106"""

    def __init__(
        self,
        *groups,
        **kwargs
    ):
        # Sprite init
        pygame.sprite.Sprite.__init__(self, *groups, **kwargs)

    def add(self, *groups):
        super().add(*groups)

    def remove(self, *groups):
        super().remove(*groups)

    def add_internal(self, group):
        super().add_internal(group)

    def remove_internal(self, group):
        super().remove_internal(group)

    def update(self, *args):
        super().update(*args)

    def kill(self):
        super().kill()

    def groups(self):
        return super().groups()

    def alive(self):
        return super().alive()


class AbstractGroup(pygame.sprite.AbstractGroup):
    """pygame: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L284
    pygame_sdl2: """

    def AbstractGroup(self):
        # Sprite init
        pygame.sprite.AbstractGroup.__init__(self)

    def sprites(self) -> list[Sprite]:
        return super().sprites()

    def add_internal(self, sprite):
        super().add_internal(sprite)

    def remove_internal(self, sprite):
        super().remove_internal(sprite)

    def has_internal(self, sprite):
        super().has_internal(sprite)

    def copy(self):
        return super().copy()

    def add(self, *sprites):
        return super().add(*sprites)

    def remove(self, *sprites):
        return super().remove(*sprites)

    def has(self, *sprites):
        return super().has(*sprites)

    def update(self, *args):
        return super().update(*args)

    def draw(self, surface):
        return super().draw(surface)

    def clear(self, surface, bgd):
        return super().clear(surface, bgd)

    def empty(self):
        return super().empty()


class Group(AbstractGroup):
    """pygame: 
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L531"""

    def __init__(self, *sprites):
        AbstractGroup.__init__(self)
        self.add(*sprites)


class RenderUpdates(Group):
    """pygame: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L557"""

    def draw(self, surface: Surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        for s in self.sprites():
            r = spritedict[s]
            newrect = surface_blit(s.image, s.rect)
            if r:
                if newrect.colliderect(r):
                    dirty_append(newrect.union(r))
                else:
                    dirty_append(newrect)
                    dirty_append(r)
            else:
                dirty_append(newrect)
            spritedict[s] = newrect
        return dirty
