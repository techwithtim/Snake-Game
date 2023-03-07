import random, os.path

#import basic pygame_sdl2 modules
import pygame_sdl2 as pygame
pygame.import_as_pygame()
pygame._optional_imports()

import renpy.store as store
import renpy.exports as renpy

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise (SystemExit, "Sorry, extended image module required")


def os_path_join(a, b):
    return a + "/" + b

#game constants
MAX_SHOTS      = 2      #most player bullets onscreen
ALIEN_ODDS     = 22     #chances a new alien appears
BOMB_ODDS      = 60    #chances a new bomb will drop
ALIEN_RELOAD   = 12     #frames between new aliens
#SCREENRECT     = Rect(0, 0, 640, 480)
SCORE          = 0


def load_image(file):
    "loads an image, prepares it for play"
    file = os_path_join('data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise (SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os_path_join('data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load,', file)
    return dummysound()



# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about

def main():
    # Initialize pygame_sdl2
    pygame.init()
    screen = pygame.display.set_mode((100,100), 32, 32)

    pygame.time.wait(1000)

    # * https://github.com/renpy/renpy/issues/4347
    # * renpytom tell me to use:
    renpy.display_reset()  # but not work

    # ! It's not work:
    renpy.call("start")

    return
