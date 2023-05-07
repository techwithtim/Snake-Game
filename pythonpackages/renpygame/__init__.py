import pythonpackages.renpygame.display as my_display
import pythonpackages.renpygame.event as my_event
import pythonpackages.renpygame.image as my_image
import pythonpackages.renpygame.mixer as my_mixer
import pythonpackages.renpygame.rect as my_rect
import pythonpackages.renpygame.sprite as my_sprite
import pythonpackages.renpygame.transform as my_transform
from pythonpackages.renpygame.renpygameCDD import (
    RenpyGameByEvent as my_RenpyGameByEvent,
)
from pythonpackages.renpygame.renpygameCDD import (
    RenpyGameByTimer as my_RenpyGameByTimer,
)
from pythonpackages.renpygame_pygame import *

Surface = my_display.Surface
Rect = my_rect.Rect
rect = my_rect
display = my_display
sprite = my_sprite
image = my_image
transform = my_transform
event = my_event
mixer = my_mixer

RenpyGameByTimer = my_RenpyGameByTimer
RenpyGameByEvent = my_RenpyGameByEvent


def init():
    return
