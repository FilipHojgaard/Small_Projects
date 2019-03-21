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

windowSurfaceObj = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('vector testing')



class Ball():
    # Attributes
    size = 50
    pos = Vector2(200,200)
    vel = Vector2(0,0)

    def __init__(self, *args):
        if (len(args) > 0):
            print("Bold lavet")
            self.pos = args[0]

    def random_speed(self):
        self.vel = Vector2(random.randint(0,4), random.randint(0,4))

    def update(self):
        print(type((self.pos)[0]))
        # self.pos += self.vel

balls = []
while True:
    windowSurfaceObj.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                print(f"Museklik på {event.pos}")
                balls.append(Ball(event.pos))
            if event.button == 3:
                for i in range(0, len(balls)):
                    if(Vector2(event.pos).distance_to(balls[i].pos) <= balls[i].size):
                        print("COLLISION DETECTED")
                        balls[i].random_speed()

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Space trykket")
                balls.append(Ball())
            if event.key == K_n:
                print(f"Number of balls: {len(balls)}")

    for i in range(0, len(balls)):
        balls[i].update()
        pygame.draw.circle(windowSurfaceObj, GREEN, balls[i].pos, balls[i].size)


    pygame.display.update()
    fpsClock.tick(FPS)
