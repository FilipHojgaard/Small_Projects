# THIS IS THE BRAIN OF THE PROGRAM. A GENETIC ALGORITHM CALCULATING AN ANSWER TO THE PROPOSED EQUATION

# Creates a binary number 0. That is 0000...0000. The bitwise ORS each bit with the bitlists value.
def bitTODec(bitlist):
    output = 0
    for bit in bitlist:
        output = (output << 1) | bit
    return output

def evaluate(user_string):
    result = eval(user_string)
    return result

# GLOBAL VARIABLES
goal = 0
popSize = 0
mutRate = 0
maxGens = 0

# API FUNCTION
def EVOLVE(equation, arg_goal, arg_popSize, arg_mutRate, arg_maxGens):
    global goal
    global popSize
    global mutRate
    global maxGens
    goal = arg_goal
    popSize = arg_popSize
    mutRate = arg_mutRate
    maxGens = arg_maxGens

# Create a generation. Can either make a new one randomized, or by a parent population
def createGeneration(*args):
    if len(args) == 0:
        # FIRST RANDOM GENERATION
        print("new random generation")
    else:
        # NEXT GENERATION BASED ON PREVIOUS
        print("Child generation from parents")
        for i in args:
            print(i)

def randomChromosone():
    pass

def fitness():
    pass






# UNIT TEST

def main():
    bitlist = [1,0,1,1,0,1] # 45
    print(bitTODec(bitlist))
    createGeneration("hej", "dig", 3)

if __name__ == "__main__":
    main()
