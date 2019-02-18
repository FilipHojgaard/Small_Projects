# // THIS IS A PARSER TO MAKE SENSE OF THE USER INPUT. TO STRUCTURE AN EQUATION WITH A NUMBER OF VARIABLES AND A RESULT TO COMPUTE IN THE GENETIC ALGORITHM.

# API function to call from another file. This parses the user input and returns a list of lists of the valid variables and arithemtic in correct order. 
def parse(user_input):
    return lexer(user_input)

def main():
    user_input = input('Enter equation: ')
    tokens = lexer(user_input)
    print(tokens)

def lexer(user_string):
    variables = []      # A list of the variables the user has entered. In userinput order.
    arithmetic = []     # A list of the arithmetic the user has entered. In userinput order.
    tokens = []         # A list of variables list and arithmetic list to send directly to the genetic algorithm.
    for i in range(0,len(user_string)):
        if not(checkCharacterVality(user_string[i])):      # Check if the user entered a invalid character
            print("ERROR: NON VALID EQUATION")
            break
        else:
            if(checkCharacterVality(user_string[i]) == 1):  # Check if the user entered a variable character
                variables.append(user_string[i])
            elif(checkCharacterVality(user_string[i]) == 2): # Check if the user entered a arithmetic character
                arithmetic.append(user_string[i])
    tokens.append(variables)
    tokens.append(arithmetic)
    return tokens

# This function takes a character and tests if it is either of the valid operations or variable names. 0 for non-valid, 1 for variable name, 2 for arithmetic.
def checkCharacterVality(char):
    if char.lower() == 'x':
        return 1
    elif char.lower() == 'y':
        return 1
    elif char.lower() == 'z':
        return 1
    elif char.lower() == 'a':
        return 1
    elif char.lower() == 'b':
        return 1
    elif char.lower() == 'c':
        return 1
    elif char.lower() == 'i':
        return 1
    elif char.lower() == 'j':
        return 1
    elif char.lower() == 'n':
        return 1
    elif char.lower() == 'm':
        return 1
    elif char.lower() == '+':
        return 2
    elif char.lower() == '-':
        return 2
    elif char.lower() == '*':
        return 2
    elif char.lower() == '/':
        return 2
    elif char.lower() == '^':
        return 2
    else:
        return 0


if __name__ == "__main__":
    main()
