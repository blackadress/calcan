import tkinter as tk
from tkinter import font as tkfont

class RectangularPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        label = tk.Label(self, text="Cálculo de canales Rectangulares",
                         font=controller.title_font)
        label.grid(row=0, column=0)

        button = tk.Button(
            self, text="Inicio",
            border=2,
            fg='red', font=controller.button_font,
            command=lambda: controller.show_frame("StartPage"))
        button.grid(row=6, column=0)
