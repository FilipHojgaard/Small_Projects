import parser_module
import ai
import tkinter as tk
import tkinter.messagebox
from tkinter import *

def execute(user_input):
    print(user_input)
    print("PARSING USER INPUT...")
    print(parser_module.parse(user_input))


def main():
    print("GUI DEVELOPMENT UNDER PROGESS")

    my_bg_color = "white"
    my_button_color = "white"

    root = tk.Tk()
    root.geometry("620x400")
    root.config(bg=my_bg_color)
    root.title("Equation Genetic Algorithm")
    root.resizable(width=False, height=False)

    def access_entry():
        execute(input.get())

    input = Entry(root, bg="old lace")
    input.place(x=160, y=100, width=180, height=25)
    calculate_button = tk.Button(root, text='Create Chromosones', command=access_entry, font='arial 8')
    calculate_button.place(x=350, y=100, width=120, height=25)





    root.mainloop()


if __name__ == "__main__":
    main()
