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
calculated_boat_coords = [0, 0]

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

def drawLine(point_a, point_b, COLOR, thickness):
    pygame.draw.line(windowsSurfaceObj, COLOR, point_a, point_b, thickness)


while(True):
    windowsSurfaceObj.fill(bg_color)
    drawLine(left_point, right_point, (0, 0, 255), 5)  # Left point to right point
    drawLine(left_point, boat_coords, (255, 0, 0), 5)  # Left point to boat
    drawLine(right_point, boat_coords, (255, 0, 0), 5) # Right point to boat
    left_angle = findAngle(boat_coords[0], boat_coords[1],
    right_point[0], right_point[1], left_point[0], left_point[1])
    right_angle = findAngle(boat_coords[0], boat_coords[1],
    left_point[0], left_point[1], right_point[0], right_point[1])
    right_angle = round((360 - right_angle), 1)

    left_angle_text = myfont.render(str(left_angle)+u"\u00b0", False, (0,0,0))
    right_angle_text = myfont.render(str(right_angle)+u"\u00b0", False, (0,0,0))

    # Calculate the length from boat to line between point_left and point_right.
    length_to_boat = (((right_point[0]-left_point[0])*math.sin(math.radians(left_angle))
    *math.sin(math.radians(right_angle)))/math.sin(math.radians(left_angle)+
    math.radians(right_angle)))
    length_to_boat = round(length_to_boat, 1)
    length_to_boat_text = myfont.render(str(length_to_boat)+ " m", False, (0,0,0))

    tangent = math.tan(math.radians(left_angle))
    adjecent = round((length_to_boat / tangent), 1)
    adjecent_text = myfont.render(str(adjecent)+" m", False, (0,0,0))

    calculated_boat_coords = [left_point[0]+adjecent, left_point[1]-length_to_boat]
    real_coords_text = myfont.render("actual: " +str(boat_coords), False, (0,0,0))
    calculated_coords_text = myfont.render("calculated: "+str(calculated_boat_coords), False, (0,0,0))

    drawLine(boat_coords, [left_point[0]+adjecent, left_point[1]], (150,150,150), 2)

    windowsSurfaceObj.blit(left_angle_text,(left_point[0]-5,left_point[1]+8))
    windowsSurfaceObj.blit(right_angle_text,(right_point[0]-5,right_point[1]+8))
    windowsSurfaceObj.blit(length_to_boat_text,(boat_coords[0],(boat_coords[1]+(length_to_boat/2))))
    windowsSurfaceObj.blit(adjecent_text,(left_point[0]+(adjecent/2), left_point[1]-20))
    windowsSurfaceObj.blit(real_coords_text,(5,5))
    windowsSurfaceObj.blit(calculated_coords_text,(50,50))


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
