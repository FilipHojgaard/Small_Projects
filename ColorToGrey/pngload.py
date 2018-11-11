import imageio
import numpy as np

im = imageio.imread('mig.png')

# Gennemsnittet af hver pixels R,G,B værdi. Så en værdi per pixel.
# Måske step 1 i at lave sort/hvid billeder. Sæt alle R,G,B til den gennemsnitlige
# værdi.
def averagePixel(im):
    pixel = []
    row = []
    picture = []
    for i in range(0,len(im)):
        for j in range(0,len(im[i])):
            for g in range(0,len(im[i][j])):
                pixel.append(im[i][j][g])
            row.append(int(sum(pixel)/len(pixel)))
            pixel = []
        picture.append(row)
        row = []
    return picture

def valueToRGB(data):
    pixel = []
    row = []
    picture = []
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            pixel.append(data[i][j])
            pixel.append(data[i][j])
            pixel.append(data[i][j])
            row.append(pixel)
            pixel = []
        picture.append(row)
        row = []
    return picture


grey = np.array(valueToRGB(averagePixel(im)))
imageio.imwrite('billedegrey.png', grey)
