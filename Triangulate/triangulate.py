import math
import pygame, sys
from pygame.locals import *
from math import atan2, degrees, pi

screen_width = 640
screen_heigh = 480

red_x = 500
red_y = 70

pygame.init()
fpsClock = pygame.time.Clock()
windowsSurfaceObj = pygame.display.set_mode((screen_width,screen_heigh))
pygame.display.set_caption("PIXEL VISUALIZATION")

bg_color = pygame.Color(200,200,250)

def findAngle(x_1, y_1, x_2, y_2, fixed_x, fixed_y):
    angle1 = atan2(y_1 - fixed_y, x_1 - fixed_x)
    angle2 = atan2(y_2 - fixed_y, x_2 - fixed_x)

    angle = angle2 - angle1
    angle = degrees(angle)
    print("Angle between lines is: " +str(angle))

def drawLine(point_a, point_b, COLOR):
    pygame.draw.line(windowsSurfaceObj, COLOR, point_a, point_b, 5)


while(True):
    windowsSurfaceObj.fill(bg_color)
    drawLine([100, 450], [red_x, red_y], (255, 0, 0))
    drawLine([100,450], [500, 250], (0, 0, 255))
    findAngle(red_x, red_y, 500, 250, 100, 450)

    keystate = pygame.key.get_pressed()
    if keystate[K_LEFT]:
        red_x -= 3
    if keystate[K_RIGHT]:
        red_x += 3
    if keystate[K_UP]:
        red_y -= 3
    if keystate[K_DOWN]:
        red_y += 3
    if keystate[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    fpsClock.tick(30)
