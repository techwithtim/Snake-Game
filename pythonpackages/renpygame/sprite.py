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

        # renpy.Displayable init
        super(Sprite, self).__init__(**kwargs)

        # pygame.sprite.Sprite init
        pygame.sprite.Sprite.__init__(self, groups)

    def renpy_render(self):
        """"""
        return


class RenderUpdates(pygame.sprite.RenderUpdates, Sprite):
    """https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.RenderUpdates"""

    def draw(self, surface) -> list:
        sprites_list: list[Sprite] = self.sprites()
        for s in sprites_list:
            if s:
                s.renpy_render()
        return super().draw(surface)
