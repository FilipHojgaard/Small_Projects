import pygame
from pygame.math import Vector2
import sys
from pygame.locals import *
import random



pygame.init()
fpsClock = pygame.time.Clock()

FPS = 30
RESOLUTION = (640, 480)
GREEN = pygame.Color(0,255,0)
WHITE = pygame.Color(255,255,255)
BLUE = pygame.Color(0,0,255)

myfont = pygame.font.SysFont('Ariel', 27)

windowSurfaceObj = pygame.display.set_mode(RESOLUTION) #, pygame.FULLSCREEN)
pygame.display.set_caption('Rotation test')


class Player():

    def __init__(self, *args):
        self.moving = False
        self.size = 20
        self.speed = 6
        self.position = Vector2(200,200)
        self.direction = Vector2(1,0)
        self.velocity = Vector2(0,0)
        self.color = pygame.Color(100,100,100)
        if (len(args)) > 0:
            if (args[0]) == 'red':
                self.color = pygame.Color(255,0,0)
            elif (args[0]) == 'blue':
                self.color = pygame.Color(0,0,255)
        print("Player created")

    def rotate_player(self, *args):
        if args[0] == 'left':
            self.direction = self.direction.rotate(-8.0)
        if args[0] == 'right':
            self.direction = self.direction.rotate(8.0)

    def forward(self):
        self.moving = True

    def break_player(self):
        self.moving = False
        self.velocity = Vector2(0,0)

    def reverse(self):
        self.velocity = self.direction*-1*0.4

    def update(self):
        if self.moving:
            self.velocity = self.direction
        self.position += self.velocity * self.speed


player = Player('blue')
player_red = Player('red')

while True:
    windowSurfaceObj.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        player.forward()
    elif keys[pygame.K_DOWN]:
        player.reverse()
    else:
        player.break_player()
    if keys[pygame.K_RIGHT]:
        player.rotate_player('right')
    if keys[pygame.K_LEFT]:
        player.rotate_player('left')
    if keys[pygame.K_w]:
        player_red.forward()
    elif keys[pygame.K_s]:
        player_red.reverse()
    else:
        player_red.break_player()
    if keys[pygame.K_d]:
        player_red.rotate_player('right')
    if keys[pygame.K_a]:
        player_red.rotate_player('left')


    player.update()
    player_red.update()
    pygame.draw.circle(windowSurfaceObj, player.color, (int(player.position[0]), int(player.position[1])), player.size)
    pygame.draw.circle(windowSurfaceObj, player_red.color, (int(player_red.position[0])+200, int(player_red.position[1])), player_red.size)

    pygame.display.update()
    fpsClock.tick(FPS)
