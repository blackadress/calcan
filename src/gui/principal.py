import tkinter as tk
from tkinter import font as tkfont

from gui.circular import CircularPage
from gui.rectangular import RectangularPage
from gui.trapecio import TrapecioPage
from gui.triangular import TriangularPage
from gui.calculadora import CalculadoraPage
from gui.parabola import ParabolaPage


class HCanalesApp(tk.Tk):
    height = 720
    width = 1080

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.geometry("{}x{}".format(self.width, self.height))

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")
        self.button_font = tkfont.Font(
            family='Helvetica', size=14, weight="bold")

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky='news')
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, CircularPage, RectangularPage, TrapecioPage, TriangularPage, ParabolaPage, CalculadoraPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    page_triangular_txt = "Cálculo de Canales Triángulares"
    page_rectangular_txt = "Cálculo de Canales Rectangulares"
    page_circular_txt = "Cálculo de Canales Circulares"
    page_trapecio_txt = "Cálculo de Canales Trapezoidales"
    page_parabola_txt = "Cálculo de Canales Parabólico"
    page_calculadora_txt = "Calculadora"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        label = tk.Label(self, text="Página Principal",
                         font=controller.title_font)
        label.grid(row=0, column=0)

        page_triangular_button = tk.Button(
            self, text=self.page_triangular_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("TriangularPage"))
        page_rectangular_button = tk.Button(
            self, text=self.page_rectangular_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("RectangularPage"))
        page_circular_button = tk.Button(
            self, text=self.page_circular_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("CircularPage"))
        page_trapecio_button = tk.Button(
            self, text=self.page_trapecio_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("TrapecioPage"))
        page_parabola_button = tk.Button(
            self, text=self.page_parabola_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("ParabolaPage"))
        page_calculadora_button = tk.Button(
            self, text=self.page_calculadora_txt,
            height=2, width=30, border=2,
            fg='green', font=controller.button_font,
            command=lambda: controller.show_frame("CalculadoraPage"))

        page_triangular_button.grid(row=1, column=0, pady=30)
        page_rectangular_button.grid(row=2, column=0, pady=30)
        page_circular_button.grid(row=3, column=0, pady=30)
        page_trapecio_button.grid(row=4, column=0, pady=30)
        page_parabola_button.grid(row=5, column=0, pady=30)
        page_calculadora_button.grid(row=6, column=0, pady=30)
