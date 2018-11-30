import imageio
import pygame, sys
from pygame.locals import *

# Average/mean is sum/len
# Median is the middle point of a dataset
# Mode is the most frequent data
im = imageio.imread('yellow.png')

# Finds the average color
def averageColor(image):
    RED = []
    GREEN = []
    BLUE = []
    # p = picture, r = row, pi = pixel.
    for p in range(0,len(image)):
        for r in range(0,len(image[p])):
            RED.append(image[p][r][0])
            GREEN.append(image[p][r][1])
            BLUE.append(image[p][r][2])

    RED_avg = sum(RED)/len(RED)
    GREEN_avg = sum(GREEN)/len(GREEN)
    BLUE_avg = sum(BLUE)/len(BLUE)

    return RED_avg, GREEN_avg, BLUE_avg
# Finds the most abundant color in the color set
def modeColor(image):
    single_hex = []
    pixels = []
    for p in range(0,len(image)):
        for r in range(0,len(image[p])):
            for pi in range(0,len(image[p][r])):
                single_hex.append(image[p][r][pi])
            pixels.append(single_hex)
            single_hex = []

    most_abundant_count = 0
    most_abundant_pixel = []
    for i in range(0,len(pixels)):
        this_abundancy = pixels.count(pixels[i])
        if (this_abundancy > most_abundant_count):
            most_abundant_count = this_abundancy
            most_abundant_pixel = pixels[i]
    return most_abundant_pixel

def paint(pixel):
    print(pixel)
    pygame.init()
    fpsClock = pygame.time.Clock()

    windowsSurfaceObj = pygame.display.set_mode((640,480))
    pygame.display.set_caption("PIXEL VISUALIZATION")

    # color = pygame.Color(pixel[0], pixel[1], pixel[2])
    r = int(pixel[0])
    g = int(pixel[1])
    b = int(pixel[2])
    color = pygame.Color(r,g,b)

    while(True):
        windowsSurfaceObj.fill(color)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(30)

# a = [[1,2],[3,4,5]]
# a.count([1,2]) returns 1

# abundant = np.max(np.bincount(image[p][r]))
# print(max)

# averageColor = averageColor(im)
# print("Average pixel is " + str(averageColor))
abundantColor = modeColor(im)
print("Most abundant pixel is " + str(abundantColor))
# paint(averageColor)
paint(abundantColor)
