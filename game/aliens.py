import random

# import basic pygame_sdl2 modules
import renpy.exports as renpy
import renpy.store as store

import pythonpackages.renpygame as pygame
from pythonpackages.renpygame.rect import Rect
from pythonpackages.renpygame.renpygameCDD import Render, RenpyGameSurface

# game constants
MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCREENRECT = Rect(0, 0, 640, 480)
SCORE = 0


class dummysound:
    def play(self): pass


# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Player(pygame.sprite.Sprite):
    speed = 10
    bounce = 24
    gun_offset = -11
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left/self.bounce % 2)

    def gunpos(self):
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top


class Alien(pygame.sprite.Sprite):
    speed = 13
    animcycle = 12
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        # TODO: has been commented pe make it work
        # self.image = self.images[self.frame/self.animcycle%3]


class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        # TODO: has been commented pe make it work
        # self.image = self.images[self.life/self.animcycle%2]
        if self.life <= 0:
            self.kill()


class Shot(pygame.sprite.Sprite):
    speed = -11
    images = []

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    speed = 9
    images = []

    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(
            midbottom=alien.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # TODO: has been commented pe make it work
        # self.font = pygame.font.Font("DejaVuSans.ttf", 20)

        # TODO: has been commented pe make it work
        # self.font.set_italic(1)
        self.color = (255, 255, 255, 255)
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            # TODO: has been commented pe make it work
            # self.image = self.font.render(msg, 0, self.color)


def main():
    screen = RenpyGameSurface(my_game)

    renpy.show_screen("renpygame_surface", surface=screen)
    renpy.call("start")
    return


def my_game(width: int, height: int, st: float, at: float) -> Render:
    # Initialize pygame
    pygame.init()

    # Set the display mode
    if store._preferences.fullscreen:
        winstyle = FULLSCREEN
    else:
        winstyle = 0

    bestdepth = pygame.display.mode_ok((0, 0), winstyle, 32)
    screen = pygame.display.set_mode((0, 0), winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = pygame.image.load('player1.gif')
    img = img.convert(width, height, st, at)
    Player.images = [img, pygame.transform.flip(img, 1, 0)]
    img = pygame.image.load('explosion1.gif')
    img = img.convert(width, height, st, at)
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Alien.images = [
        pygame.image.load('alien1.gif').convert(width, height, st, at),
        pygame.image.load('alien2.gif').convert(width, height, st, at),
        pygame.image.load('alien3.gif').convert(width, height, st, at),
    ]
    Bomb.images = [pygame.image.load(
        'bomb.gif').convert(width, height, st, at)]
    Shot.images = [pygame.image.load(
        'shot.gif').convert(width, height, st, at)]

    # decorate the game window
    icon = pygame.transform.scale(Alien.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = pygame.image.load('background.gif')
    bgdtile = bgdtile.convert(width, height, st, at)
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    # assign default groups to each sprite class
    Player.containers = all
    Alien.containers = aliens, all, lastalien
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    # Create Some Starting Values
    global score
    alienreload = ALIEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    global SCORE
    SCORE = 0

    # initialize our starting sprites
    player = Player()
    Alien()  # note, this 'lives' because it goes into a sprite group

    # TODO: has been commented pe make it work
    # if pygame.font:
    #     all.add(Score())

    while player.alive():

        # TODO: has been commented pe make it work
        # get input
        # for event in pygame.event.get():
        #     if event.type == QUIT or \
        #         (event.type == KEYDOWN and event.key == K_ESCAPE):
        #             return SCORE
        # keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # TODO: has been commented pe make it work
        # handle player input
        # direction = keystate[K_RIGHT] - keystate[K_LEFT]
        # player.move(direction)
        # firing = keystate[K_SPACE]
        # if not player.reloading and firing and len(shots) < MAX_SHOTS:
        #     Shot(player.gunpos())
        #     shoot_sound.play()
        # player.reloading = firing

        # Create new alien
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            Alien()
            alienreload = ALIEN_RELOAD

        # Drop bombs
        if lastalien and not int(random.random() * BOMB_ODDS):
            Bomb(lastalien.sprite)

        # Detect collisions
        for alien in pygame.sprite.spritecollide(player, aliens, 1):
            # boom_sound.play()
            Explosion(alien)
            Explosion(player)
            SCORE = SCORE + 1
            player.kill()

        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            # boom_sound.play()
            Explosion(alien)
            SCORE = SCORE + 1

        for bomb in pygame.sprite.spritecollide(player, bombs, 1):
            # boom_sound.play()
            Explosion(player)
            Explosion(bomb)
            player.kill()

        # draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(40)

    pygame.time.wait(1000)

    return screen
