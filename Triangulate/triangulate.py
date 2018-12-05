import math
import pygame, sys
from pygame.locals import *
from math import atan2, degrees, pi

screen_width = 1280
screen_heigh = 720

boat_coords = [400, 150]
left_point = [100, 650]
right_point = [600, 650]
red_x = 500
red_y = 70

pygame.init()
fpsClock = pygame.time.Clock()
windowsSurfaceObj = pygame.display.set_mode((screen_width,screen_heigh))
pygame.display.set_caption("Triangulate Math Visualisation")

bg_color = pygame.Color(200,200,250)

pygame.font.init()
myfont = pygame.font.SysFont('Ariel', 27)

def findAngle(x_1, y_1, x_2, y_2, fixed_x, fixed_y):
    angle1 = atan2(y_1 - fixed_y, x_1 - fixed_x)
    angle2 = atan2(y_2 - fixed_y, x_2 - fixed_x)

    angle = angle2 - angle1
    angle = degrees(angle)
    return round(angle, 1)

def drawLine(point_a, point_b, COLOR):
    pygame.draw.line(windowsSurfaceObj, COLOR, point_a, point_b, 5)


while(True):
    windowsSurfaceObj.fill(bg_color)
    drawLine(left_point, right_point, (0, 0, 255))  # Left point to right point
    drawLine(left_point, boat_coords, (255, 0, 0))  # Left point to boat
    drawLine(right_point, boat_coords, (255, 0, 0)) # Right point to boat
    left_angle = findAngle(boat_coords[0], boat_coords[1],
    right_point[0], right_point[1], left_point[0], left_point[1])
    right_angle = findAngle(boat_coords[0], boat_coords[1],
    left_point[0], left_point[1], right_point[0], right_point[1])
    right_angle = round((360 - right_angle), 1)

    left_angle_text = myfont.render(str(left_angle)+u"\u00b0", False, (0,0,0))
    right_angle_text = myfont.render(str(right_angle)+u"\u00b0", False, (0,0,0))

    windowsSurfaceObj.blit(left_angle_text,(left_point[0]-5,left_point[1]+8))
    windowsSurfaceObj.blit(right_angle_text,(right_point[0]-5,right_point[1]+8))

    keystate = pygame.key.get_pressed()
    if keystate[K_LEFT]:
        boat_coords[0] -= 3
    if keystate[K_RIGHT]:
        boat_coords[0] += 3
    if keystate[K_UP]:
        boat_coords[1] -= 3
    if keystate[K_DOWN]:
        boat_coords[1] += 3
    if keystate[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    fpsClock.tick(30)
