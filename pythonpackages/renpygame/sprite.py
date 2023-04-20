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


class RenderUpdates(pygame.sprite.RenderUpdates):
    """pygame: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates
    pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/sprite.py#L557"""

    def draw(self, surface: Surface) -> list:
        return super().draw(surface)
