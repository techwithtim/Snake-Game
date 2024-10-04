import math
import random
import pygame
import random
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500

cols = 25
rows = 20


# start screen to help users distinguish when the program begins instead of being thrown into game
def start_screen():
    global win
    win.fill((0, 0, 0)) # background black
    font = pygame.font.SysFont('arial', 20)
    two_font = pygame.font.SysFont('arial', 15, italic = True)
    starting = font.render('Press "s" to Start', True, (255, 255, 255)) # start option is larger
    ending = two_font.render('Press "q" to Quit', True, (255, 255, 255)) # end is smaller and italic

    # positioning the
    win.blit(starting, (width // 2 - starting.get_width() // 2, height // 2.2 - starting.get_height() // 2))
    win.blit(ending, (width // 1.85 - starting.get_width() // 2, height // 1.9 - starting.get_height() // 2))
    pygame.display.update()

    # Wait for the player to press spacebar
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    waiting = False
            keys = pygame.key.get_pressed()

            # game exits if you press q
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

# similar to start screen, this allows user more control on when to start or exit game
def end_screen():
    global win
    win.fill((0, 0, 0))  # background black
    font = pygame.font.SysFont('arial', 20)
    two_font = pygame.font.SysFont('arial', 15, italic = True)
    # add ending screen quit or restart options
    label = font.render('Press "s" to Start Again', True, (255, 255, 255))
    ending = two_font.render('Press "q" to Quit Game', True, (255, 255, 255))

    # Position the label in the center of the screen
    win.blit(label, (width // 2 - label.get_width() // 2, height // 2.2 - label.get_height() // 2))

    # add ending screen label
    win.blit(ending, (width // 1.8 - label.get_width() // 2, height // 1.9 - label.get_height() // 2))
    pygame.display.update()

    # wait for user to press a buttion
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if user presses "s," start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    waiting = False
            keys = pygame.key.get_pressed()

            # game exits if you press q
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

class cube():
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(85, 126, 235), image=None): # changed snake to blue
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny # "L", "R", "U", "D"
        self.color = color
        self.image = image

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        if self.image:
            # put picture of apple as snack where there is snack
            surface.blit(self.image, (i * dis, j * dis))
        else:
            # draw regular background if else
            pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake():
    body = []
    turns = {}

    def __init__(self, color, pos):
        # pos is given as coordinates on the grid ex (1,5)
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            # game exits if you press q!! issue addressed
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirny = -1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirny = 1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def redrawWindow():
    global win
    win.fill((145, 214, 75)) # changed to green background (like grass)
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    pygame.display.update()


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (14, 64, 6), (x, 0), (x, w)) # grid lines a dark green
        pygame.draw.line(surface, (14, 64, 6), (0, y), (w, y))


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1, rows - 1)
        y = random.randrange(1, rows - 1)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def main():
    pygame.init()
    global s, snack, win
    win = pygame.display.set_mode((width, height))

    start_screen()
    s = snake((0, 0, 255), (10, 10))
    s.addCube()

    # load image of snake snack (i chose an apple)
    snake_snack = pygame.image.load('snake_snack.jpg')  # replace 'snack_image.png' with the snack image you choose
    snake_snack = pygame.transform.scale(snake_snack, (width // rows, width // rows))  # scale
    snack = cube(randomSnack(rows, s), image=snake_snack)

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        headPos = s.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))
            end_screen()

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), image=snake_snack)

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score:", len(s.body))
                s.reset((10, 10))


        redrawWindow()


main()
