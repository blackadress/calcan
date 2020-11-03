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

        ## adding left frame (datos)
        datos_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        datos_frame.grid(row=1, column=0, columnspan=6, sticky='w', padx=(50, 10))
        datos_frame.config(border=3)
        datos_frame.columnconfigure(0, weight=1)

        ## Titulo Datos
        titulo = tk.Label(datos_frame, text='Datos')
        titulo.grid(row=0, column=0, columnspan=3)
        titulo.config(fg='blue')

        ## Datos > Caudal
        caudal_label = tk.Label(datos_frame, text='Caudal (Q)', height=2)
        caudal_label.grid(row=1, column=0)
        caudal_entry = tk.Entry(datos_frame)
        caudal_entry.grid(row=1, column=1)
        caudal_label = tk.Label(datos_frame, text='m3/s', height=2)
        caudal_label.grid(row=1, column=2)
        caudal_label.config(padx=4)

        ## Datos > Ancho de Solera
        ancho_solera_label = tk.Label(datos_frame, text='Ancho de solera (b)', height=2)
        ancho_solera_label.grid(row=2, column=0)
        ancho_solera_entry = tk.Entry(datos_frame)
        ancho_solera_entry.grid(row=2, column=1)
        ancho_solera_label = tk.Label(datos_frame, text='m', height=2)
        ancho_solera_label.grid(row=2, column=2)
        ancho_solera_label.config(padx=4)

        ## Datos > Talud
        talud_label = tk.Label(datos_frame, text='Talud (Z)', height=2)
        talud_label.grid(row=3, column=0)
        talud_entry = tk.Entry(datos_frame)
        talud_entry.grid(row=3, column=1)
        talud_label = tk.Label(datos_frame, text='', height=2)
        talud_label.grid(row=3, column=2)
        talud_label.config(padx=4)

        ## adding right frame (imagen)
        img_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        img_frame.grid(row=1, column=1, columnspan=6, rowspan=4, sticky='e', padx=(10, 50))
        img_frame.config(border=2)
        img_frame.columnconfigure(0, weight=1)

        ## Img > label_img
        # PIL
        # img= ImageTk.PhotoImage(Image.open("img/rectangular.png"))
        # img = img.resize((300, 250), Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(img)
        # img_label = tk.Label(image=img)

        # no PIL
        img = tk.PhotoImage(file='img/rectangular.png')
        img_label = tk.Label(img_frame)
        img_label.image = img
        img_label.configure(image=img)

        img_label.grid(row=0, column=0, columnspan=12, rowspan=6)

        button = tk.Button(
            self, text="Inicio",
            border=2,
            fg='red', font=controller.button_font,
            command=lambda: controller.show_frame("StartPage"))
        button.grid(row=6, column=0)
