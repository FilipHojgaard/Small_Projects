# // THIS IS A PARSER TO MAKE SENSE OF THE USER INPUT. TO STRUCTURE AN EQUATION WITH A NUMBER OF VARIABLES AND A RESULT TO COMPUTE IN THE GENETIC ALGORITHM.

# API function to call from another file. This parses the user input and returns a list of lists of the valid variables and arithemtic in correct order.
def parse(user_input):
    return lexer(user_input)


def lexer(user_string):
    number_of_variables = 0
    variables = []      # A list of the variables the user has entered. In userinput order.
    arithmetic = []     # A list of the arithmetic the user has entered. In userinput order.
    tokens = []         # A list of variables list and arithmetic list to send directly to the genetic algorithm.
    for i in range(0,len(user_string)):
        if not(checkCharacterVality(user_string[i])):           # Check if the user entered a invalid character
            print("ERROR: NON VALID EQUATION")
            break
        else:
            if(checkCharacterVality(user_string[i]) == 1):      # Check if the user entered a variable character
                number_of_variables += 1
                variables.append(user_string[i])
            elif(checkCharacterVality(user_string[i]) == 2):    # Check if the user entered a arithmetic character
                arithmetic.append(user_string[i])
    tokens.append(variables)
    tokens.append(arithmetic)
    return (user_string, number_of_variables)

# This function takes a character and tests if it is either of the valid operations or variable names. 0 for non-valid, 1 for variable name, 2 for arithmetic. 3 for numbers.
def checkCharacterVality(char):
    if char.lower() in 'xyzabcijnm':
        return 1
    elif char.lower() in '+-*/**()':
        return 2
    elif char.isdigit():
        return 3
    else:
        return 0

# UNIT TEST
def main():
    user_input = input('Enter equation: ')
    tokens = lexer(user_input)
    print(tokens)

if __name__ == "__main__":
    main()
