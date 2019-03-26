import pygame
from pygame.math import Vector2
import sys
from pygame.locals import *
import random



pygame.init()
fpsClock = pygame.time.Clock()

FPS = 30
RESOLUTION = (1920, 1080)
GREEN = pygame.Color(0,255,0)
WHITE = pygame.Color(255,255,255)

myfont = pygame.font.SysFont('Ariel', 27)

windowSurfaceObj = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)
pygame.display.set_caption('vector testing')


class Ball():
    # Attributes
    size = 20
    pos = Vector2(200,200)
    vel = Vector2(0,0)
    gravity = 0
    gravity_reference = 0.5
    Rcolor = 0
    Gcolor = 0
    Bcolor = 0
    color = 0

    def __init__(self, *args):
        if (len(args) > 0):
            self.pos = args[0]
            while(True):
                self.vel = Vector2(random.randint(-2,2), random.randint(-2,2))
                if (not(self.vel == Vector2(0,0))):
                    break

            self.Rcolor = random.randint(0,255)
            self.Gcolor = random.randint(0,255)
            self.Bcolor = random.randint(0,255)
            self.color = pygame.Color(self.Rcolor,self.Gcolor,self.Bcolor)
            # self.toggleGravity() # Start out with gravity

    def collision(self):
        if (self.pos[0] < 0-self.size) or (self.pos[0] > RESOLUTION[0]+self.size) or (self.pos[1]) < 0-self.size or (self.pos[1] > RESOLUTION[1]+self.size):
            return True

    def toggleGravity(self):
        if self.gravity == 0:
            self.gravity = self.gravity_reference
        else:
            self.gravity = 0

    def random_speed(self):
        self.vel = Vector2(random.randint(-2,2), random.randint(-2,2))

    def update(self):
        self.vel[1] += self.gravity
        self.pos += self.vel

balls = []
while True:
    windowSurfaceObj.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                balls.append(Ball(event.pos))
            if event.button == 3:
                for i in range(0, len(balls)):
                    if(Vector2(event.pos).distance_to(balls[i].pos) <= balls[i].size):
                        balls[i].random_speed()

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                for i in range(0,100):
                    balls.append(Ball(Vector2(random.randint(0,RESOLUTION[0]), random.randint(0,RESOLUTION[1]))))
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_r:
                del balls[:]
            if event.key == K_g:
                for i in range(0, len(balls)):
                    balls[i].toggleGravity()




    for i in range(len(balls)-1, -1, -1):
        balls[i].update()
        if balls[i].collision():
            del balls[i]
        else:
            pygame.draw.circle(windowSurfaceObj, balls[i].color, (int(balls[i].pos[0]), int(balls[i].pos[1])), balls[i].size)



    number_of_balls_text = myfont.render("Balls: "+str(len(balls)), False, (0,0,0))
    windowSurfaceObj.blit(number_of_balls_text,(10,10))

    pygame.display.update()
    fpsClock.tick(FPS)
