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
    moving = False
    size = 20
    speed = 6
    position = Vector2(200,200)
    direction = Vector2(1,0)
    velocity = Vector2(0,0)
    color = pygame.Color(0,0,255)

    def __init__(self, *args):
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


player = Player()


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


    player.update()
    pygame.draw.circle(windowSurfaceObj, player.color, (int(player.position[0]), int(player.position[1])), player.size)

    pygame.display.update()
    fpsClock.tick(FPS)
