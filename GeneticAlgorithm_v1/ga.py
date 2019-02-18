import random
from operator import itemgetter # For sorting a list og list on a specific index in the inner list
import sys

# CHROMOSONE ENCODING / DECODING MEANING:
# 0 0 0 = 0
# 0 0 1 = 1
# 0 1 0 = 2
# 0 1 1 = 3
# 1 0 0 = 4
# 1 0 1 = 5
# 1 1 0 = 6
# 1 1 1 = 7

# GOAL IS TO FIND SOLVE A ARITHMETIC EQUATION OF (A^B-C)/(D*E+F) = X.
# GOAL: X = 24
# FINTESS: Answer - Goal = Fitness

def main():
    # VARIABLES
    goal = 30
    population_amount = 100
    chromosone_length = 18
    cross_rate = 0.7
    mutation_rate_probability = 0.1

    # GENETIC ALGORITHM
    population = create_population(population_amount, chromosone_length) # Creates a population of random chromosnes.
    gen_1 = new_generation(population, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_2 = new_generation(gen_1, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_3 = new_generation(gen_2, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_4 = new_generation(gen_3, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_5 = new_generation(gen_4, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_6 = new_generation(gen_5, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_7 = new_generation(gen_6, goal, population_amount, cross_rate, mutation_rate_probability)
    gen_8 = new_generation(gen_7, goal, population_amount, cross_rate, mutation_rate_probability)


def new_generation(population, goal, population_amount, cross_rate, mutation_rate_probability):
    new_generation = []
    population = test_chromosone(population, goal) # Tests the population of chromosones and calculates a fitness score to each of them.
    while(len(new_generation) < population_amount):
        parent_1 = roulette_wheel_selection(population)     # Find 2 parents in population using roulette_wheel_selection
        parent_2 = roulette_wheel_selection(population)
        child_1, child_2 = cross_over_rate(parent_1, parent_2, cross_rate)
        child_1, child_2 = mutation_rate(child_1, child_2, mutation_rate_probability)
        new_generation.append(child_1)
        new_generation.append(child_2)
    print("_________GENERATION END__________")
    return new_generation



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
        temp = random.randint(0,100)
        if (temp > 50):
            chromosone.append(1)
        else:
            chromosone.append(0)
    return(chromosone)

# Select a parent. The chromosones with the highest fitness score has the highest probability of being choosen.
def roulette_wheel_selection(population):
    fitness_sum = 0
    parent = []                                         # Allocate memory to a parent chromosone
    for i in range(0,len(population)):                  # Calculate a fitness sum from the whole population
        fitness_sum += population[i][-1]
    print("fitness sum: " +str(fitness_sum))
    fixed_point = random.randint(0,fitness_sum)         # Generate a random fixed_point from 0 to the fitness sum
    print("Random fixed point: " + str(fixed_point))
    partial_sum = 0                                     # Partial sum is added up. When this exceeds the threshold, fixed_point, we choose the current chromosone as a parent.
    for i in range(0,len(population)):
        # If the partial_sum exceeds the fitness_sum. (Because the fixed_point is too close to fitness_sum, and is incremented too much)
        if(partial_sum >= fitness_sum):
            parent = population[i-1]
            break
        # When the threshold is found normally
        elif(partial_sum >= fixed_point):
            parent = population[i]                      # Sets parent to be the winner
            break
        else:
            partial_sum += population[i][-1]
    # If no parent was choosen, the worst chromosone is choosen.
    if (parent == []):
        parent = population[-1]
    return parent[:-1]

def cross_over_rate(parent_1, parent_2, cross_rate):
    child_1 = []
    child_2 = []
    if (random.uniform(0,1) < cross_rate):                     # If a random number between 0 and 1 is under 0,7 then we make a cross over
        swap_position = random.randint(0,len(parent_1)-1) # -2 since: -1(we dismiss the fitness score position) -1 (it doesnt make sense to swap after the last bit anyway) = -2
        print("CROSS OVER")
        print(swap_position)
        child_1[:swap_position] = parent_1[:swap_position]
        child_1[swap_position:] = parent_2[swap_position:]
        child_2[:swap_position] = parent_2[:swap_position]
        child_2[swap_position:] = parent_1[swap_position:]
        print(child_1)
        print(child_2)
        return (child_1, child_2)

    else:
        print("NO CROSS OVER")
        return (parent_1, parent_2)

def mutation_rate(child_1, child_2, mutation_rate):
    print("BEFORE MUTATION: ")
    print(child_1)
    print(child_2)
    for i in range(0, len(child_1)):
        mutation_change = 100/mutation_rate
        if (random.randint(0,mutation_change) == 1):
            if (child_1[i] == 0):
                child_1[i] = 1
            else:
                child_1[i] = 0
    for i in range(0, len(child_2)):
        if (random.randint(0,100/mutation_rate) == 1):
            if (child_2[i] == 0):
                child_2[i] = 1
            else:
                child_2[i] = 0
    print("AFTER MUTATION: ")
    print(child_1)
    print(child_2)
    return (child_1, child_2)


def test_chromosone(population, goal):
    for i in range(0, len(population)):
        print(population[i])
        A = decode(population[i][0:3])          # Find the decoded value of the first 3 bits of the chromosones
        B = decode(population[i][3:6])
        C = decode(population[i][6:9])
        D = decode(population[i][9:12])          # Find the decoded value of the first 3 bits of the chromosones
        E = decode(population[i][12:15])
        F = decode(population[i][15:18])
        print(A,B,C)
        try:
            guess = int((A**B-C)/(D*E+F))                           # Calcuate the guess frmo the decoded chromosone information
        except:
            print("SKIPPED TEST: Division by 0")
            guess = 0
        print("guess: " + str(guess))
        fitness = abs(guess - goal)                  # Calculate a fitness score based on the guess and the goal
        print("fitness: " + str(fitness))
        population[i].append(fitness)           # Appends the fitness score to after the chromosone data
        if (fitness == 0):
            finnish(population[i])
    return(revertFitness(population))                          # Returns the whole poplation list of lists.

# Sorts the population from best to worst. Then Swaps the best chromosones fitness with the worst, the second best with the second worst etc. So a Roulette wheel selection is possible.
def revertFitness(population):
    fitness_index = len(population[0])-1        # Finds the index where the fitness score is stored
    population = sorted(population, key=itemgetter(fitness_index))   # Sorts the whole population on the fitness_index. Lowest(best) fitness first.
    # CREATE A COPY ONLY OF FITNESS
    fitness_array = []
    for i in range(0,len(population)):
        fitness_array.append(population[i][fitness_index])
    print(fitness_array)
    # SWAP THE BEST FITNESS WITH WORST, SECOND BEST WITH SECOND WORST ETC. USE COPY ARRAY TO POINT BACKWARDS
    for i in range(0,len(population)):
        population[i][fitness_index] = fitness_array[-1-i]
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

def finnish(chromosone):
    print("WE HAVE AN ANSWER BY CHROMOSONE:")
    print(chromosone)
    A = decode(chromosone[0:3])          # Find the decoded value of the first 3 bits of the chromosones
    B = decode(chromosone[3:6])
    C = decode(chromosone[6:9])
    D = decode(chromosone[9:12])          # Find the decoded value of the first 3 bits of the chromosones
    E = decode(chromosone[12:15])
    F = decode(chromosone[15:18])
    print("(" + str(A) + "^" + str(B) + "-" + str(C) + ") / (" + str(D) + "*" + str(E) + "+" + str(F) + ") = 30")
    sys.exit("EXITED WITH SUCCES")


if __name__ == "__main__":
    main()
