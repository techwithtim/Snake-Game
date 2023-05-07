from typing import Optional

import pythonpackages.renpygame_pygame as pygame
from pythonpackages.renpygame_pygame.event import *

# https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx


class EventType(pygame.event.EventType):  # type: ignore
    """ "pygame_sdl2: https://github.com/renpy/pygame_sdl2/blob/master/src/pygame_sdl2/event.pyx#LL58C1-L97C1
    pygame: https://www.pygame.org/docs/ref/event.html#pygame.event.Event"""

    @property
    def dict(self):
        return super().dict

    @property
    def type(self) -> int:
        return super().type

    @property
    def key(self) -> Optional[int]:
        return super().key
