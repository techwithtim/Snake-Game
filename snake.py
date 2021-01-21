import math
import random
import pygame
import random
import tkinter as tk
from tkinter import *


width = 700
height = 700
cols = 25
rows = 25

pygame.init()
clock = pygame.time.Clock()
background = pygame.display.set_mode((width, height))


window=Tk()
window.title("NEW Snake Game")
window.geometry('300x100+470+200')

label1=Label(window, text="Game Start\nLet's go",width=30,height=5,fg="blue",relief="solid")
label1.pack()

b1=Button(window,text="시작하기",width=10,height=5,bg='yellow',command = window.destroy)
b1.pack()

window.mainloop()


class cube():
    rows = 25
    w = 700
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny 
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)


    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))

        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

            

class snake():
    body = []
    turns = {}
    
    def __init__(self, color, pos):
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

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirny = -1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirny = 1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx,c.dirny)

        level = int(len(self.body) / 5)
        fps = 6 + (1.5*level)
        clock.tick(fps)
        
    def reset(self,pos):
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
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
    
    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
    
    def end_game():
        print("Score:", len(self.body))
        sys.exit(0)
        

    def show_info(self):
        font = pygame.font.SysFont('malgungothic',30,bold=5)
        image = font.render(f'  {len(self.body)} .Lv  ', True, (0,0,0))
        pos = image.get_rect()
        pos.move_ip(20,20)
        pygame.draw.rect(image, (0,0,0),(pos.x-15, pos.y-15, pos.width, pos.height), 2)
        background.blit(image, pos)


def finish_game(seconds):
        fin=Tk()
        fin.title("Full Level")
        fin.geometry('300x100+500+200')
        b=int(seconds)
        print ("Total Time :", b)
        label2=Label(fin, text="SUCCESS\nTotal Time :"+str(b),width=30,height=5,fg="red",relief="solid")
        label2.pack()
    
        
        fin.mainloop()


def redrawWindow():
    global win
    win.fill((176,224,230))
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    s.show_info()
    pygame.display.update()
    pass

def drawGrid(w, rows, surface):

    sizeBtwn = w // rows
    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (150,150,150), (x, 0),(x,w))
        pygame.draw.line(surface, (150,150,150), (0, y),(w,y))


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
               continue
        else:
               break

    return (x,y)


def main():
    global s, snack, win, b
    win = pygame.display.set_mode((width,height))
    s = snake((255,0,0), (10,10))
    s.addCube()
    snack = cube(randomSnack(rows,s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    start_ticks=pygame.time.get_ticks()


    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        headPos = s.head.pos
        seconds=(pygame.time.get_ticks()-start_ticks)/1000

        if headPos[0] >= 25 or headPos[0] < 0 or headPos[1] >= 25 or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s), color=(0,255,0))
            
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score:", len(s.body))
                s.reset((10,10))
                break

        if len(s.body) > 25:
            finish_game(seconds)
            end_game()
            
        redrawWindow()

main()
    