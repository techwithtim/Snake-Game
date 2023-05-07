import random
from typing import Optional

import renpy.exports as renpy
import renpy.store as store

import pythonpackages.renpygame as pygame
from pythonpackages.renpygame.event import EventType
from pythonpackages.renpygame.rect import Rect
from pythonpackages.renpygame.sprite import RenderUpdates

# game constants
MAX_SHOTS = 2  # most player bullets onscreen
ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCREENRECT = Rect(0, 0, 640, 480)


class dummysound:
    def play(self):
        pass


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
    images: list[pygame.Surface] = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left / self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top


class Alien(pygame.sprite.Sprite):
    speed = 13
    animcycle = 12
    images: list[pygame.Surface] = []

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
    images: list[pygame.Surface] = []

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
    images: list[pygame.Surface] = []

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
    images: list[pygame.Surface] = []

    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)

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
        if sh.score != self.lastscore:
            self.lastscore = sh.score
            msg = "Score: %d" % sh.score
            # TODO: has been commented pe make it work
            # self.image = self.font.render(msg, 0, self.color)


class SharedDataAlienGame:
    def __init__(self):
        self.all = None
        self.player = None
        self.background = None
        self.lastalien = None
        self.aliens = None
        self.bombs = None
        self.shots = None
        self.alienreload = 12
        self.score = 0
        self.player_have_shot = False
        self.player_move = 0  # -1 left, 0 no move, 1 right
        self.boom_sound = pygame.mixer.Sound("audio/boom.wav")
        self.shoot_sound = pygame.mixer.Sound("audio/car_door.wav")

    @property
    def all(self) -> RenderUpdates:
        return self._all

    @all.setter
    def all(self, value: RenderUpdates):
        self._all = value

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player):
        self._player = value

    @property
    def background(self) -> pygame.Surface:
        return self._background

    @background.setter
    def background(self, value: pygame.Surface):
        self._background = value

    @property
    def lastalien(self) -> int:
        return self._lastalien

    @lastalien.setter
    def lastalien(self, value: int):
        self._lastalien = value

    @property
    def aliens(self) -> RenderUpdates:
        return self._aliens

    @aliens.setter
    def aliens(self, value: RenderUpdates):
        self._aliens = value

    @property
    def bombs(self) -> RenderUpdates:
        return self._bombs

    @bombs.setter
    def bombs(self, value: RenderUpdates):
        self._bombs = value

    @property
    def shots(self) -> RenderUpdates:
        return self._shots

    @shots.setter
    def shots(self, value: RenderUpdates):
        self._shots = value


sh = SharedDataAlienGame()
# Create Some Starting Values
kills = 0
clock = pygame.time.Clock()


def main():
    # # Initialize a shared data
    global sh

    if not sh:
        sh = SharedDataAlienGame()

    # Initialize a game
    displayable_with_logic = pygame.RenpyGameByTimer(
        first_step=my_game_first_step,
        update_process=my_game_logic,
        event_lambda=game_event,
        delay=0.04,
    )
    # show amd start the game
    displayable_with_logic.show()

    # * after show() the game will be running when the game is over

    # clean up the shared data
    score = sh.score
    sh = None
    # return to renpy
    return score


def my_game_first_step(width: int, height: int, st: float, at: float) -> pygame.Surface:
    # Set the display mode
    if store._preferences.fullscreen:
        winstyle = FULLSCREEN
    else:
        winstyle = 0

    bestdepth = pygame.display.mode_ok((0, 0), winstyle, 32)
    screen = pygame.display.set_mode((0, 0), winstyle, bestdepth)

    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = pygame.image.load("player1.gif")
    img_flip = pygame.transform.flip(img, 1, 0)
    img = img.convert(st, at)
    img_flip = img_flip.convert(st, at)
    Player.images = [img, img_flip]
    img = pygame.image.load("explosion1.gif")
    img_flip = pygame.transform.flip(img, 1, 0)
    img = img.convert(st, at)
    img_flip = img_flip.convert(st, at)
    Explosion.images = [img, img_flip]
    Alien.images = [
        pygame.image.load("alien1.gif").convert(st, at),
        pygame.image.load("alien2.gif").convert(st, at),
        pygame.image.load("alien3.gif").convert(st, at),
    ]
    Bomb.images = [pygame.image.load("bomb.gif").convert(st, at)]
    Shot.images = [pygame.image.load("shot.gif").convert(st, at)]

    # decorate the game window
    pygame.display.set_icon(pygame.image.load("alien1.gif").pygame_image)
    pygame.display.set_caption("Pygame Aliens")
    pygame.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = pygame.image.load("background.gif")
    bgdtile = bgdtile.convert(st, at)
    sh.background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        sh.background.blit(bgdtile, (x, 0))
    screen.blit(sh.background, (0, 0))
    pygame.display.flip()

    # play music
    pygame.mixer.music.load("audio/house_lo.wav")
    pygame.mixer.music.play(-1)

    # Initialize Game Groups
    sh.aliens = pygame.sprite.Group()
    sh.shots = pygame.sprite.Group()
    sh.bombs = pygame.sprite.Group()
    sh.all = pygame.sprite.RenderUpdates()
    sh.lastalien = pygame.sprite.GroupSingle()

    # assign default groups to each sprite class
    Player.containers = sh.all
    Alien.containers = sh.aliens, sh.all, sh.lastalien
    Shot.containers = sh.shots, sh.all
    Bomb.containers = sh.bombs, sh.all
    Explosion.containers = sh.all
    Score.containers = sh.all

    # initialize our starting sprites
    sh.player = Player()
    Alien()  # note, this 'lives' because it goes into a sprite group

    # TODO: has been commented pe make it work
    # if pygame.font:
    #     all.add(Score())

    return screen


def my_game_logic(
    cur_screen: pygame.Surface,
    st: float,
    at: float,
    next_frame_time: float,
    current_frame_number: int,
) -> Optional[float]:
    if sh.player.alive():
        # clear/erase the last drawn sprites
        sh.all.clear(cur_screen, sh.background)

        # update all the sprites
        sh.all.update()

        # handle player input
        direction = sh.player_move
        sh.player.move(direction)
        if sh.player_have_shot and len(sh.shots) < MAX_SHOTS:
            Shot(sh.player.gunpos())
            # TODO: has been commented pe make it work
            sh.shoot_sound.play()

        # Create new alien
        if sh.alienreload:
            sh.alienreload = sh.alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            Alien()
            sh.alienreload = ALIEN_RELOAD

        # Drop bombs
        if sh.lastalien and not int(random.random() * BOMB_ODDS):
            Bomb(sh.lastalien.sprite)

        # Detect collisions
        for alien in pygame.sprite.spritecollide(sh.player, sh.aliens, 1):
            sh.boom_sound.play()
            Explosion(alien)
            Explosion(sh.player)
            sh.score = sh.score + 1
            sh.player.kill()

        for alien in pygame.sprite.groupcollide(sh.shots, sh.aliens, 1, 1).keys():
            sh.boom_sound.play()
            Explosion(alien)
            sh.score = sh.score + 1

        for bomb in pygame.sprite.spritecollide(sh.player, sh.bombs, 1):
            sh.boom_sound.play()
            Explosion(sh.player)
            Explosion(bomb)
            sh.player.kill()

        # draw the scene
        dirty = sh.all.draw(cur_screen)
        pygame.display.update(dirty)

        return next_frame_time
    else:
        # game end
        return None


def game_event(ev: EventType, x: int, y: int, st: float):
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
        sh.player_have_shot = True
    elif ev.type == pygame.KEYUP and ev.key == pygame.K_SPACE:
        sh.player_have_shot = False
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
        sh.player_move = -1
    elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
        if sh.player_move == -1:
            sh.player_move = 0
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
        sh.player_move = 1
    elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
        if sh.player_move == 1:
            sh.player_move = 0
    return
