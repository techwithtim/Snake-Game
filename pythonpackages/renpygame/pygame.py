import pygame_sdl2 as pygame
from pygame import *

pygame.import_as_pygame()
pygame._optional_imports()

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise (SystemExit, "renpygame: Sorry, extended image module required")
