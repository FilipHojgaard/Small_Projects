import random

# CHROMOSONE ENCOTION / DECOTION MEANING:
# 0 0 0 = 0
# 0 0 1 = 1
# 0 1 0 = 2
# 0 1 1 = 3
# 1 0 0 = 4
# 1 0 1 = 5
# 1 1 0 = 6
# 1 1 1 = 7

# GOAL IS TO FIND SOLVE A ARITHMETIC EQUATION OF A*B+C = X.
# GOAL: X = 23
# FINTESS: Answer - Goal = Fitness

def main():
    # VARIABLES
    goal = 24
    population_amount = 2
    chromosone_length = 9

    # GENETIC ALGORITHM
    population = create_population(population_amount, chromosone_length) # Number of chromosones, length of each chromosone
    print(test_chromosone(population, goal))



# Using the "random_chromosone" helping function. This function creates a population of 'amount' random chromosones with each being 'chromosone_length' long.
def create_population(amount, chromosone_length):
    chromosone_array = []
    for x in range(0,amount):
        chromosone_array.append(random_chromosone(chromosone_length))  # Choose the length of the chromosone here
    return(chromosone_array)

# This is a helping function for the 'create_population' function. It creates a random chromosone at a specific length.
def random_chromosone(chromosone_length):
    chromosone = []
    for x in range(chromosone_length):
        temp = random.randint(1,101)
        if (temp > 50):
            chromosone.append(1)
        else:
            chromosone.append(0)
    return(chromosone)

def test_chromosone(population, goal):
    for i in range(0, len(population)):
        print(population[i])
        A = decode(population[i][0:3])
        B = decode(population[i][3:6])
        C = decode(population[i][6:9])
        print(A,B,C)
        guess = A*B+C
        print("guess: " + str(guess))
        fitness = guess - goal
        print("fitness: " + str(fitness))
        population[i].append(fitness)
    return(population)

def decode(code):
    if(code == [0,0,0]):
        return 0
    elif(code == [0,0,1]):
        return 1
    elif(code == [0,1,0]):
        return 2
    elif(code == [0,1,1]):
        return 3
    elif(code == [1,0,0]):
        return 4
    elif(code == [1,0,1]):
        return 5
    elif(code == [1,1,0]):
        return 6
    elif(code == [1,1,1]):
        return 7
    else:
        print("ERROR: NO DECODE MATCH FOUND")
        return 99




if __name__ == "__main__":
    main()
