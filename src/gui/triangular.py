import tkinter as tk
from tkinter import font as tkfont
# from PIL import Image, ImageTk

from gui.ecuaciones import numero_de_froude, pendiente_critica, tirante_critico_triangular, area_hidraulica_triangular, espejo_de_agua_triangular, perimetro_mojado_triangular, radio_hidraulico_triangular, velocidad_triangular, energia_especifica_triangular


class TriangularPage(tk.Frame):
    internacional = True

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        label = tk.Label(self, text="Cálculo de canales Triangulares",
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
        self.caudal_entry = tk.Entry(datos_frame)
        self.caudal_entry.grid(row=1, column=1)
        self.caudal_label = tk.Label(datos_frame, text='m3/s', height=2)
        self.caudal_label.grid(row=1, column=2)
        self.caudal_label.config(padx=4)

        ## Datos > Talud
        talud_label = tk.Label(datos_frame, text='Talud (Z)', height=2)
        talud_label.grid(row=2, column=0)
        self.talud_entry = tk.Entry(datos_frame)
        self.talud_entry.grid(row=2, column=1)
        self.talud_label = tk.Label(datos_frame, text='', height=2)
        self.talud_label.grid(row=2, column=2)
        self.talud_label.config(padx=4)

        # Datos > Internacional/Ingles
        cambio_unidades_btn = tk.Button(
            datos_frame, text='SI/Ingles',
            border=2, pady=8,
            fg='blue',
            command=self.cambio_unidades
        )
        cambio_unidades_btn.grid(row=3, column=0, rowspan=3)

        # adding right frame (imagen)
        img_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        img_frame.grid(row=1, column=6, columnspan=6,
                       rowspan=4, sticky='e', padx=(10, 50))
        img_frame.config(border=2)
        img_frame.columnconfigure(0, weight=1)

        # no PIL
        img = tk.PhotoImage(file='img/triangular.png')
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
            row=9, column=0, columnspan=6, rowspan=4, sticky='w', padx=(50, 10), pady=30)
        results_frame_left.config(border=2)
        results_frame_left.columnconfigure(0, weight=1)

        # Resultados > Tirante crítico (y)
        tirante_critico_label = tk.Label(
            results_frame_left, text='Tirante crítico (y)', height=2)
        tirante_critico_label.grid(row=0, column=0)
        # tirante_critico_entry = tk.Entry(results_frame_left)
        self.tirante_critico_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        self.tirante_critico_entry.grid(row=0, column=1)
        self.tirante_critico_label = tk.Label(
            results_frame_left, text='m', height=2)
        self.tirante_critico_label.grid(row=0, column=2)
        self.tirante_critico_label.config(padx=4)

        # Resultados > Área hidráulica (A) m2
        area_label = tk.Label(results_frame_left,
                              text='Área hidráulica (A)', height=2)
        area_label.grid(row=1, column=0)
        # area_entry = tk.Entry(results_frame_left)
        self.area_entry = tk.Label(results_frame_left, text='00.0000', height=2)
        self.area_entry.grid(row=1, column=1)
        self.area_label = tk.Label(results_frame_left, text='m2', height=2)
        self.area_label.grid(row=1, column=2)
        self.area_label.config(padx=4)

        # Resultados > Espejo de agua (T) m
        espejo_agua_label = tk.Label(
            results_frame_left, text='Espejo de agua (T)', height=2)
        espejo_agua_label.grid(row=2, column=0)
        # espejo_agua_entry = tk.Entry(results_frame_left)
        self.espejo_agua_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        self.espejo_agua_entry.grid(row=2, column=1)
        self.espejo_agua_label = tk.Label(results_frame_left, text='m', height=2)
        self.espejo_agua_label.grid(row=2, column=2)
        self.espejo_agua_label.config(padx=4)

        # Resultados > Número de Froude
        numero_froude_label = tk.Label(
            results_frame_left, text='Número de Froude', height=2)
        numero_froude_label.grid(row=3, column=0)
        # numero_froude_entry = tk.Entry(results_frame_left)
        self.numero_froude_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        self.numero_froude_entry.grid(row=3, column=1)
        self.numero_froude_label = tk.Label(results_frame_left, text='', height=2)
        self.numero_froude_label.grid(row=3, column=2)
        self.numero_froude_label.config(padx=4)

        # Resultados > Pendiente hidráulica
        pendiente_hidraulica_label = tk.Label(
            results_frame_left, text='Pendiente hidráulica', height=2)
        pendiente_hidraulica_label.grid(row=4, column=0)
        # pendiente_hidraulica_entry = tk.Entry(results_frame_left)
        self.pendiente_hidraulica_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        self.pendiente_hidraulica_entry.grid(row=4, column=1)
        self.pendiente_hidraulica_label = tk.Label(results_frame_left, text='', height=2)
        self.pendiente_hidraulica_label.grid(row=4, column=2)
        self.pendiente_hidraulica_label.config(padx=4)

        # adding bottom right frame (datos)
        results_frame_right = tk.Frame(
            bottom_frame, border=2, relief=tk.RAISED)
        results_frame_right.grid(
            row=6, column=4, columnspan=6, rowspan=4, sticky='e', padx=(10, 10), pady=30)
        results_frame_right.config(border=3)
        results_frame_right.columnconfigure(0, weight=1)

        ## Resultados > Perímetro
        perimetro_label = tk.Label(
            results_frame_right, text='Perímetro (p)', height=2)
        perimetro_label.grid(row=0, column=0)
        # self.perimetro_entry = tk.Entry(results_frame_right)
        self.perimetro_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        self.perimetro_entry.grid(row=0, column=1)
        self.perimetro_label = tk.Label(results_frame_right, text='m', height=2)
        self.perimetro_label.grid(row=0, column=2)
        self.perimetro_label.config(padx=4)

        # Resultados > Radio hidráulico m
        radio_hidraulico_label = tk.Label(
            results_frame_right, text='Radio hidráulico (R)', height=2)
        radio_hidraulico_label.grid(row=1, column=0)
        # radio_hidraulico_entry = tk.Entry(results_frame_right)
        self.radio_hidraulico_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        self.radio_hidraulico_entry.grid(row=1, column=1)
        self.radio_hidraulico_label = tk.Label(
            results_frame_right, text='m', height=2)
        self.radio_hidraulico_label.grid(row=1, column=2)
        self.radio_hidraulico_label.config(padx=4)

        ## Resultados > Velocidad
        velocidad_label = tk.Label(
            results_frame_right, text='Velocidad', height=2)
        velocidad_label.grid(row=2, column=0)
        # velocidad_entry = tk.Entry(results_frame_right)
        self.velocidad_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        self.velocidad_entry.grid(row=2, column=1)
        self.velocidad_label = tk.Label(results_frame_right, text='m/s', height=2)
        self.velocidad_label.grid(row=2, column=2)
        self.velocidad_label.config(padx=4)

        # Resultados > Energía específica
        energia_especifica_label = tk.Label(
            results_frame_right, text='Energía específica (E)', height=2)
        energia_especifica_label.grid(row=3, column=0)
        # self.energia_especifica_entry = tk.Entry(results_frame_right)
        self.energia_especifica_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        self.energia_especifica_entry.grid(row=3, column=1)
        self.energia_especifica_label = tk.Label(
            results_frame_right, text='m', height=2)
        self.energia_especifica_label.grid(row=3, column=2)
        self.energia_especifica_label.config(padx=4)

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

        self.error_msg = tk.Label(
            self, height=2, fg='red', font=controller.button_font)
        self.error_msg.grid(row=19, column=0, columnspan=12)

    def get_values(self):
        Q = self.caudal_entry.get()
        Z = self.talud_entry.get()

        try:
            Q = float(Q)
            Z = float(Z)
            return (Q, Z)
        except ValueError:
            self.error_msg.config(text="Ingrese números válidos")
            return (1, 1, 1)

    def calcular(self):
        n = 1
        (Q, Z) = self.get_values()
        y = tirante_critico_triangular(Q, Z, self.internacional)
        A = area_hidraulica_triangular(y, Z, self.internacional)
        T = espejo_de_agua_triangular(y, Z, self.internacional)
        P = perimetro_mojado_triangular(y, Z, self.internacional)
        R = radio_hidraulico_triangular(A, P, self.internacional)
        v = velocidad_triangular(y, self.internacional)
        E = energia_especifica_triangular(y, v, self.internacional)
        F = numero_de_froude(v, A, T, self.internacional)
        S = pendiente_critica(Q, n, A, R, self.internacional)

        ## mostrando los datos en la GUI
        self.tirante_critico_entry.config(text="{:.5f}".format(y))
        self.area_entry.config(text="{:.5f}".format(A))
        self.espejo_agua_entry.config(text="{:.5f}".format(T))
        self.numero_froude_entry.config(text="{:.5f}".format(F))
        self.pendiente_hidraulica_entry.config(text="{:.5f}".format(S))
        self.perimetro_entry.config(text="{:.5f}".format(P))
        self.radio_hidraulico_entry.config(text="{:.5f}".format(R))
        self.velocidad_entry.config(text="{:.5f}".format(v))
        self.energia_especifica_entry.config(text="{:.5f}".format(E))

        print(y, A, T, F, P, R, v, E)
        print(S)
        print('calcular')

    def limpiar(self):
        self.caudal_entry.delete(0, tk.END)
        self.caudal_entry.insert(0, '')
        self.talud_entry.delete(0, tk.END)
        self.talud_entry.insert(0, '')
        print('limpiar')

    def exportar(self):
        print('exportar')

    def cambio_unidades(self):
        self.internacional = not self.internacional
        if self.internacional:
            self.caudal_label.config(text="m3/s")
            self.talud_label.config(text="m")

            self.tirante_critico_label.config(text="m")
            self.area_label.config(text="m2")
            self.espejo_agua_label.config(text="m")
            self.numero_froude_label.config(text="")
            self.pendiente_hidraulica_label.config(text="")
            self.perimetro_label.config(text="m")
            self.radio_hidraulico_label.config(text="m")
            self.velocidad_label.config(text="m/s")
            self.energia_especifica_label.config(text="m-Kg/Kg")

        else:
            self.caudal_label.config(text="ft3/s")
            self.talud_label.config(text="ft")

            self.tirante_critico_label.config(text="ft")
            self.area_label.config(text="ft2")
            self.espejo_agua_label.config(text="ft")
            self.numero_froude_label.config(text="")
            self.pendiente_hidraulica_label.config(text="")
            self.perimetro_label.config(text="ft")
            self.radio_hidraulico_label.config(text="ft")
            self.velocidad_label.config(text="ft/s")
            self.energia_especifica_label.config(text="ft-Kg/Kg")

        print('cambio unidades')
