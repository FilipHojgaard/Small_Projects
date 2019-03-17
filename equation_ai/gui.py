import parser_module
import ai
import tkinter as tk
import tkinter.messagebox
from tkinter import *

def execute(user_input):
    print(user_input)
    print("PARSING USER INPUT...")
    print(parser_module.lexer(user_input))


def main():

    # POPULATION AMOUNT N
    # CROSS RATE 0.7
    # MUTATION RATE
    # MAX GENERATIONS

    print("GUI DEVELOPMENT UNDER PROGESS")

    WHITE = "white"

    root = tk.Tk()
    root.geometry("620x400")
    root.config(bg=WHITE)
    root.title("Equation Genetic Algorithm")
    root.resizable(width=False, height=False)

    def access_entry():
        execute(input.get())

    # EQUATION FIELDS
    equation_label = Label(root, bg=WHITE, text='Equation:', font='arial 9')
    equation_label.place(x=200, y=70, width=100, height=25)

    input = Entry(root, bg=WHITE)
    input.place(x=120, y=100, width=160, height=25)

    equal_label = Label(root, bg=WHITE, text='=', font='arial 8')
    equal_label.place(x=280, y=100, width=20, height=25)

    goal = Entry(root, bg=WHITE)
    goal.place(x=300, y=100, width=50, height=25)

    # PARAMETER FIELDS
    pop_label = Label(root, bg=WHITE, text='Population Size:', font='arial 8')
    pop_label.place(x=120, y=150, width=80, height=25)
    population_size = Entry(root, bg=WHITE)
    population_size.place(x=250, y=150, width=50, height=25)
    population_size.insert(0,'100')

    mutation_label = Label(root, bg=WHITE, text='Mutation Rate:', font='arial 8')
    mutation_label.place(x=120, y=200, width=80, height=25)
    mutation_rate = Entry(root, bg=WHITE)
    mutation_rate.place(x=250, y=200, width=50, height=25)
    mutation_rate.insert(0,'1')

    maxGen_label = Label(root, bg=WHITE, text='Max Generations:', font='arial 8')
    maxGen_label.place(x=120, y=250, width=100, height=25)
    max_generations = Entry(root, bg=WHITE)
    max_generations.place(x=250, y=250, width=40, height=25)
    max_generations.insert(0,'1000')

    # EVOLVE BUTTON
    calculate_button = tk.Button(root, text='EVOLVE', command=access_entry, font='arial 10')
    calculate_button.place(x=250, y=350, width=100, height=45)

    root.mainloop()


if __name__ == "__main__":
    main()
