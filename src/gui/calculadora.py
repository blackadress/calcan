import tkinter as tk
import parser
from tkinter import font as tkfont


class CalculadoraPage(tk.Frame):
    i = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller

        frame = tk.Frame(self, border=2, relief=tk.RAISED)
        frame.grid(row=0, column=0, columnspan=6)
        frame.config(border=3)
        frame.columnconfigure(0, weight=1)

        self.display = tk.Entry(frame, font=controller.button_font)
        self.display.grid(row=1, column=0, columnspan=6, sticky='w')

        # Numeric Buttons
        tk.Button(frame, text="1", height=3, width=4,
                  command=lambda: self.get_numbers(1)).grid(row=2, column=0)
        tk.Button(frame, text="2", height=3, width=4,
                  command=lambda: self.get_numbers(2)).grid(row=2, column=1)
        tk.Button(frame, text="3", height=3, width=4,
                  command=lambda: self.get_numbers(3)).grid(row=2, column=2)

        tk.Button(frame, text="4", height=3, width=4,
                  command=lambda: self.get_numbers(4)).grid(row=3, column=0)
        tk.Button(frame, text="5", height=3, width=4,
                  command=lambda: self.get_numbers(5)).grid(row=3, column=1)
        tk.Button(frame, text="6", height=3, width=4,
                  command=lambda: self.get_numbers(6)).grid(row=3, column=2)

        tk.Button(frame, text="7", height=3, width=4,
                  command=lambda: self.get_numbers(7)).grid(row=4, column=0)
        tk.Button(frame, text="8", height=3, width=4,
                  command=lambda: self.get_numbers(8)).grid(row=4, column=1)
        tk.Button(frame, text="9", height=3, width=4,
                  command=lambda: self.get_numbers(9)).grid(row=4, column=2)

        # Bottom Buttons
        tk.Button(frame, text="AC", height=3, width=4,
                  command=lambda: self.clear_display()).grid(row=5, column=0)
        tk.Button(frame, text="0", height=3, width=4,
                  command=lambda: self.get_numbers(0)).grid(row=5, column=1)
        tk.Button(frame, text="%", height=3, width=4,
                  command=lambda: self.get_operation("%")).grid(row=5, column=2)

        tk.Button(frame, text="+", height=3, width=4,
                  command=lambda: self.get_operation("+")).grid(row=2, column=3)
        tk.Button(frame, text="-", height=3, width=4,
                  command=lambda: self.get_operation("-")).grid(row=3, column=3)
        tk.Button(frame, text="*", height=3, width=4,
                  command=lambda: self.get_operation("*")).grid(row=4, column=3)
        tk.Button(frame, text="/", height=3, width=4,
                  command=lambda: self.get_operation("/")).grid(row=5, column=3)

        # More Math Operators
        tk.Button(frame, text="⟵", height=3, width=4, command=lambda: self.undo()).grid(
            row=2, column=4, sticky='we', columnspan=2)
        tk.Button(frame, text="exp", height=3, width=4,
                  command=lambda: self.get_operation("**")).grid(row=3, column=4)
        tk.Button(frame, text="^2", height=3, width=4,
                  command=lambda: self.get_operation("**2")).grid(row=3, column=5)
        tk.Button(frame, text="(", height=3, width=4, command=lambda: self.get_operation(
            "(")).grid(row=4, column=4, sticky='we')
        tk.Button(frame, text=")", height=3, width=4, command=lambda: self.get_operation(
            ")")).grid(row=4, column=5, sticky='we')
        tk.Button(frame, text="=", height=3, width=4, command=lambda: self.calculate()).grid(
            row=5, column=4, sticky='we', columnspan=2)

    def get_numbers(self, n):
        self.display.insert(self.i, n)
        self.i += 1

    def get_operation(self, operator):
        opertor_length = len(operator)
        self.display.insert(self.i, operator)
        self.i += opertor_length

    def calculate(self):
        display_state = self.display.get()
        try:
            math_expression = parser.expr(display_state).compile()
            result = eval(math_expression)
            self.clear_display()
            self.display.insert(0, result)
        except Exception:
            self.clear_display()
            self.display.insert(0, 'Error')

    def clear_display(self):
        self.display.delete(0, tk.END)

    def undo(self):
        display_state = self.display.get()
        if len(display_state):
            display_new_state = display_state[:-1]
            self.clear_display()
            self.display.insert(0, display_new_state)
        else:
            self.clear_display()
            self.display.insert(0, 'Error')
