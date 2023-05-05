# * This library is used to link renpygame to a pygame library (Now pygame_sdl2, but it can be changed to pygame)

from pygame_sdl2 import *

import pythonpackages.renpygame_pygame.display as pygame_display
import pythonpackages.renpygame_pygame.event as pygame_event
import pythonpackages.renpygame_pygame.image as pygame_image
import pythonpackages.renpygame_pygame.rect as pygame_rect
import pythonpackages.renpygame_pygame.sprite as pygame_sprite
import pythonpackages.renpygame_pygame.transform as pygame_transform

rect = pygame_rect
display = pygame_display
sprite = pygame_sprite
image = pygame_image
transform = pygame_transform
event = pygame_event
