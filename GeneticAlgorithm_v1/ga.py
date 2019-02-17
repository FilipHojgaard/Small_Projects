import random



def main():
    print(create_population(6, 16)) # Number of chromosones, length of each chromosone



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







if __name__ == "__main__":
    main()
