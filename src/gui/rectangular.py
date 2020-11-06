import tkinter as tk
from tkinter import font as tkfont


class RectangularPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        label = tk.Label(self, text="Cálculo de canales Rectangulares",
                         font=controller.title_font)
        label.grid(row=0, column=0, columnspan=12)

        # adding left frame (datos)
        datos_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        datos_frame.grid(row=1, column=0, columnspan=6,
                         sticky='w', padx=(50, 10))
        datos_frame.config(border=3)
        datos_frame.columnconfigure(0, weight=1)

        # Titulo Datos
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

        # Datos > Ancho de Solera
        ancho_solera_label = tk.Label(
            datos_frame, text='Ancho de solera (b)', height=2)
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

        # adding right frame (imagen)
        img_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        img_frame.grid(row=1, column=6, columnspan=6,
                       rowspan=4, sticky='e', padx=(10, 50))
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

        # adding bottom frame full
        bottom_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        bottom_frame.grid(
                row=6, column=0, columnspan=12, rowspan=4, sticky='we', padx=10, pady=30)
        bottom_frame.config(border=2)
        bottom_frame.columnconfigure(0, weight=1)

        # Titulo Resultados
        titulo = tk.Label(bottom_frame, text='Resultados')
        titulo.grid(row=0, column=0, columnspan=12)
        titulo.config(fg='blue')

        # adding bottom frame left (results)
        results_frame_left = tk.Frame(bottom_frame, border=2, relief=tk.RAISED)
        results_frame_left.grid(
            row=6, column=0, columnspan=6, rowspan=4, sticky='w', padx=(50, 10), pady=30)
        results_frame_left.config(border=2)
        results_frame_left.columnconfigure(0, weight=1)

        # Resultados > Tirante crítico (y)
        tirante_critico_label = tk.Label(
            results_frame_left, text='Tirante crítico (y)', height=2)
        tirante_critico_label.grid(row=0, column=0)
        tirante_critico_entry = tk.Entry(results_frame_left)
        tirante_critico_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        tirante_critico_entry.grid(row=0, column=1)
        tirante_critico_label = tk.Label(
            results_frame_left, text='m', height=2)
        tirante_critico_label.grid(row=0, column=2)
        tirante_critico_label.config(padx=4)

        # Resultados > Área hidráulica (A) m2
        area_label = tk.Label(results_frame_left,
                              text='Área hidráulica (A)', height=2)
        area_label.grid(row=1, column=0)
        # area_entry = tk.Entry(results_frame_left)
        area_entry = tk.Label(results_frame_left, text='00.0000', height=2)
        area_entry.grid(row=1, column=1)
        area_label = tk.Label(results_frame_left, text='m2', height=2)
        area_label.grid(row=1, column=2)
        area_label.config(padx=4)

        # Resultados > Espejo de agua (T) m
        espejo_agua_label = tk.Label(
            results_frame_left, text='Espejo de agua (T)', height=2)
        espejo_agua_label.grid(row=2, column=0)
        # espejo_agua_entry = tk.Entry(results_frame_left)
        espejo_agua_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        espejo_agua_entry.grid(row=2, column=1)
        espejo_agua_label = tk.Label(results_frame_left, text='m', height=2)
        espejo_agua_label.grid(row=2, column=2)
        espejo_agua_label.config(padx=4)

        # Resultados > Número de Froude
        numero_froude_label = tk.Label(
            results_frame_left, text='Número de Froude', height=2)
        numero_froude_label.grid(row=3, column=0)
        # numero_froude_entry = tk.Entry(results_frame_left)
        numero_froude_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        numero_froude_entry.grid(row=3, column=1)
        numero_froude_label = tk.Label(results_frame_left, text='', height=2)
        numero_froude_label.grid(row=3, column=2)
        numero_froude_label.config(padx=4)

        # adding bottom right frame (datos)
        results_frame_right = tk.Frame(bottom_frame, border=2, relief=tk.RAISED)
        results_frame_right.grid(
            row=6, column=4, columnspan=6, rowspan=4, sticky='e', padx=(10, 10), pady=30)
        results_frame_right.config(border=3)
        results_frame_right.columnconfigure(0, weight=1)

        ## Resultados > Perímetro
        perimetro_label = tk.Label(
            results_frame_right, text='Perímetro (p)', height=2)
        perimetro_label.grid(row=0, column=0)
        perimetro_entry = tk.Entry(results_frame_right)
        # perimetro_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        perimetro_entry.grid(row=0, column=1)
        perimetro_label = tk.Label(results_frame_right, text='m', height=2)
        perimetro_label.grid(row=0, column=2)
        perimetro_label.config(padx=4)

        # Resultados > Radio hidráulico m
        radio_hidraulico_label = tk.Label(
            results_frame_right, text='Radio hidráulico (R)', height=2)
        radio_hidraulico_label.grid(row=1, column=0)
        radio_hidraulico_entry = tk.Entry(results_frame_right)
        # radio_hidraulico_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        radio_hidraulico_entry.grid(row=1, column=1)
        radio_hidraulico_label = tk.Label(
            results_frame_right, text='m', height=2)
        radio_hidraulico_label.grid(row=1, column=2)
        radio_hidraulico_label.config(padx=4)

        ## Resultados > Velocidad
        velocidad_label = tk.Label(
            results_frame_right, text='Velocidad', height=2)
        velocidad_label.grid(row=2, column=0)
        velocidad_entry = tk.Entry(results_frame_right)
        # velocidad_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        velocidad_entry.grid(row=2, column=1)
        velocidad_label = tk.Label(results_frame_right, text='m/s', height=2)
        velocidad_label.grid(row=2, column=2)
        velocidad_label.config(padx=4)

        # Resultados > Energía específica
        energia_especifica_label = tk.Label(
            results_frame_right, text='Energía específica (E)', height=2)
        energia_especifica_label.grid(row=3, column=0)
        energia_especifica_entry = tk.Entry(results_frame_right)
        # energia_especifica_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        energia_especifica_entry.grid(row=3, column=1)
        energia_especifica_label = tk.Label(
            results_frame_right, text='m', height=2)
        energia_especifica_label.grid(row=3, column=2)
        energia_especifica_label.config(padx=4)

        calcular_btn = tk.Button(
            self, text='Calcular',
            border=2,
            fg='blue', font=controller.button_font,
            command=self.calcular
        )
        calcular_btn.grid(row=18, column=0)
        # calcular_btn.config(padx=20)

        limpiar_btn = tk.Button(
            self, text='Limpiar campos',
            border=2,
            fg='purple3', font=controller.button_font,
            command=self.limpiar
        )
        limpiar_btn.grid(row=18, column=3)

        exportar_btn = tk.Button(
            self, text='Exportar a PDF',
            border=2,
            fg='dark green', font=controller.button_font,
            command=self.exportar
        )
        exportar_btn.grid(row=18, column=7)

        home_btn = tk.Button(
            self, text="Inicio",
            border=2,
            fg='red', font=controller.button_font,
            command=lambda: controller.show_frame("StartPage"))
        home_btn.grid(row=18, column=9)

    def calcular(self):
        print('calcular')

    def limpiar(self):
        print('limpiar')

    def exportar(self):
        print('exportar')
