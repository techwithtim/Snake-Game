import renpy.exports as renpy
from pygame_sdl2.sprite import *

import pythonpackages.renpygame.pygame as pygame


class Sprite(renpy.Displayable, pygame.sprite.Sprite):
    """https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite"""

    def __init__(
        self,
        *groups,
        **kwargs
    ):

        self.__g = {}  # The groups the sprite is in
        if groups:
            self.add(*groups)

        # renpy.Displayable init
        super(Sprite, self).__init__(**kwargs)

    def renpy_render(self):
        """"""
        return


class RenderUpdates(pygame.sprite.RenderUpdates):
    """https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates"""

    def draw(self, surface) -> list:
        sprites_list: list[Sprite] = self.sprites()
        for s in sprites_list:
            if s:
                s.renpy_render()
        return super().draw(surface)
