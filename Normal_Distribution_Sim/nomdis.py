import sys;
import matplotlib.pyplot as plt;
from random import uniform;

'''
This is a normal distribution simulator.
If a call of 'map.py 10 5' is called then 5 vectors of length 10, is made.
Then a change of normal distribution is made by finding the middle point
in this case '5'. Then the index number is dividied by this middle point.
So that the middle will be 1.0, and the edges will be large numbers.
Then these numbers will go in a random function from 0.0 to this number. If it
is between 0.0 and 1.0 it will be a zero. Otherwise a 1.
Then a histogram will be made of all these 5 vectors with a count to see,
hopefully a beautifully made normal distribution of one's and zero's.
'''

def ArgTest():
    if (len(sys.argv) < 3):
        print("ERROR: Not enough arguments. x and y required")
    elif not(sys.argv[1].isdigit() & sys.argv[2].isdigit()):
        print("ERROR: Arguments must be numbers")
    else:
        return int(sys.argv[1]), int(sys.argv[2])

def makeMatrix(a, b):
    matrix = [0] * b
    for i in range(len(matrix)):
        matrix[i] = VectorDistribution(a)
    return matrix

def VectorDistribution(l):
    vector = [0] * l
    result = [0] * l
    middle = l/2
    # ulige = 0, lige = 1
    if ((l % 2) == 0):
        n = 1
    else:
        n = 0
    for i in range(1,len(vector)+1):
        if (i <= middle):
            oneChange = float(middle)/float(i)
        else:
            oneChange = float(middle)/float(i-n)
            n += 2
        # print("value: " + str(oneChange))
        vector[i-1] = oneChange
        r = uniform(0.0, oneChange)
        # print("r: " + str(r))
        if ((r > 0.0) & (r < 1.0)):
            result[i-1] = 1
        else:
            result[i-1] = 0
    # print(vector)
    # print(result)
    return result

def Count(matrix):
    distribution = [0] * len(matrix[0])
    result = []
    print(matrix)
    # print(len(matrix))
    for i in range(0, len(matrix[0])):
        distribution[i] = [j[i] for j in matrix]
    print(distribution)
    for i in range(len(distribution)):
        result.append(sum(distribution[i]))
    print(result)
    return result


def Main():
    a, b = ArgTest()
    # VectorDistribution(a)
    fin = Count(makeMatrix(a, b))
    plt.plot(fin)
    plt.show()

Main()
