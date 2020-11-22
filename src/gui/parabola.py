import xlwt
import fpdf
import tkinter as tk
from tkinter import font as tkfont

from gui.ecuaciones import *

class ParabolaPage(tk.Frame):
    internacional = True

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.controller = controller
        label = tk.Label(self, text="Cálculo de canales parabólicos",
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

        # Datos > Ancho de Solera
        espejo_agua_label = tk.Label(
            datos_frame, text='Espejo de agua (T)', height=2)
        espejo_agua_label.grid(row=2, column=0)
        self.espejo_agua_entry = tk.Entry(datos_frame)
        self.espejo_agua_entry.grid(row=2, column=1)
        self.espejo_agua_label = tk.Label(datos_frame, text='m', height=2)
        self.espejo_agua_label.grid(row=2, column=2)
        self.espejo_agua_label.config(padx=4)

        # Datos > coeficiente de friccion
        coef_friccion_label = tk.Label(
            datos_frame, text='Coeficiente de fricción', height=2)
        coef_friccion_label.grid(row=3, column=0)
        self.coef_friccion_entry = tk.Entry(datos_frame)
        self.coef_friccion_entry.insert(0, 1)
        self.coef_friccion_entry.grid(row=3, column=1)
        self.coef_friccion_label = tk.Label(datos_frame, text='', height=2)
        self.coef_friccion_label.grid(row=3, column=2)
        self.coef_friccion_label.config(padx=4)

        # Datos > Internacional/Ingles
        cambio_unidades_btn = tk.Button(
            datos_frame, text='SI/Ingles',
            border=2, pady=8,
            fg='blue',
            command=self.cambio_unidades
        )
        cambio_unidades_btn.grid(row=4, column=0, rowspan=3)

        # adding right frame (imagen)
        img_frame = tk.Frame(self, border=2, relief=tk.RAISED)
        img_frame.grid(row=1, column=6, columnspan=6,
                       rowspan=4, sticky='e', padx=(10, 50))
        img_frame.config(border=2)
        img_frame.columnconfigure(0, weight=1)

        # no PIL
        img = tk.PhotoImage(file='img/parabolico.png')
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
        self.tirante_critico_entry = tk.Entry(results_frame_left)
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
        foco_parabola_label = tk.Label(
            results_frame_left, text='Foco parábola', height=2)
        foco_parabola_label.grid(row=2, column=0)
        # foco_parabola_entry = tk.Entry(results_frame_left)
        self.foco_parabola_entry = tk.Label(
            results_frame_left, text='00.0000', height=2)
        self.foco_parabola_entry.grid(row=2, column=1)
        self.foco_parabola_label = tk.Label(results_frame_left, text='m', height=2)
        self.foco_parabola_label.grid(row=2, column=2)
        self.foco_parabola_label.config(padx=4)

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
        results_frame_right = tk.Frame(bottom_frame, border=2, relief=tk.RAISED)
        results_frame_right.grid(
            row=6, column=4, columnspan=6, rowspan=4, sticky='e', padx=(10, 240), pady=30)
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
        self.velocidad_entry = tk.Label(results_frame_right, text='00.0000', height=2)
        self.velocidad_entry.grid(row=2, column=1)
        self.velocidad_label = tk.Label(results_frame_right, text='m/s', height=2)
        self.velocidad_label.grid(row=2, column=2)
        self.velocidad_label.config(padx=4)

        # Resultados > Energía específica
        energia_especifica_label = tk.Label(
            results_frame_right, text='Energía específica (E)', height=2)
        energia_especifica_label.grid(row=3, column=0)
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
        limpiar_btn.grid(row=18, column=2)

        exportar_pdf_pdf_btn = tk.Button(
            self, text='Exportar a PDF',
            border=2,
            fg='dark green', font=controller.button_font,
            command=self.exportar_pdf,
        )
        exportar_pdf_pdf_btn.grid(row=18, column=4, padx=(50, 10))

        exportar_excel_btn = tk.Button(
            self, text='Exportar a excel',
            border=2,
            fg='dark green', font=controller.button_font,
            command=self.exportar_excel
        )
        exportar_excel_btn.grid(row=18, column=7)

        home_btn = tk.Button(
            self, text="Inicio",
            border=2,
            fg='red', font=controller.button_font,
            command=lambda: controller.show_frame("StartPage"))
        home_btn.grid(row=18, column=8)

        self.error_msg = tk.Label(
            self, height=2, fg='red', font=controller.button_font)
        self.error_msg.grid(row=19, column=0, columnspan=12)

    def get_values(self):
        Q = self.caudal_entry.get()
        T = self.espejo_agua_entry.get()
        n = self.coef_friccion_entry.get()

        try:
            Q = float(Q)
            T = float(T)
            n = float(n)
            return (Q, T, n)
        except ValueError:
            self.error_msg.config(text="Ingrese números válidos")
            return (1, 1, 1)


    def calcular(self):
        (Q, T, n) = self.get_values()
        y = tirante_critico_parabolico(Q, T, self.internacional)
        A = area_hidraulica_parabolico(y, T, self.internacional)
        P = perimetro_mojado_parabolico(T, y, A, self.internacional)
        R = radio_hidraulico_parabolico(A, P, self.internacional)
        v = velocidad_parabolico(Q, A, self.internacional)
        k = foco_parabola(T, y, self.internacional)
        E = energia_especifica_parabolico(y, v, self.internacional)
        F = numero_de_froude(v, A, T, self.internacional)
        S = pendiente_critica(Q, n, A, R, self.internacional)

        ## mostrando los datos en la GUI
        self.tirante_critico_entry.config(text="{:.5f}".format(y))
        self.area_entry.config(text="{:.5f}".format(A))
        self.foco_parabola_entry.config(text="{:.5f}".format(k))
        self.numero_froude_entry.config(text="{:.5f}".format(F))
        self.pendiente_hidraulica_entry.config(text="{:.5f}".format(S))
        self.perimetro_entry.config(text="{:.5f}".format(P))
        self.radio_hidraulico_entry.config(text="{:.5f}".format(R))
        self.velocidad_entry.config(text="{:.5f}".format(v))
        self.energia_especifica_entry.config(text="{:.5f}".format(E))

        print(y, A, T, P, R, v, E)
        print(S)

        print('calcular')

    def limpiar(self):
        self.caudal_entry.delete(0, tk.END)
        self.caudal_entry.insert(0, '')
        self.espejo_agua_entry.delete(0, tk.END)
        self.espejo_agua_entry.insert(0, '')
        self.coef_friccion_entry.delete(0, tk.END)
        self.coef_friccion_entry.insert(0, 1)
        print('limpiar')

    def exportar_excel(self):
        Caudal = self.caudal_entry.get()
        Espejo_agua = self.espejo_agua_entry.get()
        Coef_friccion = self.coef_friccion_entry.get()
        tirante_critico = self.tirante_critico_entry.cget("text")
        area = self.area_entry.cget("text")
        foco_parabola = self.foco_parabola_entry.cget("text")
        numero_froude = self.numero_froude_entry.cget("text")
        pendiente_hidraulica = self.pendiente_hidraulica_entry.cget("text")
        perimetro = self.perimetro_entry.cget("text")
        radio_hidraulico = self.radio_hidraulico_entry.cget("text")
        velocidad = self.velocidad_entry.cget("text")
        energia_especifica = self.energia_especifica_entry.cget("text")

        wb = xlwt.Workbook()
        # añadiendo datos a la hoja de excel
        hoja_1 = wb.add_sheet('Hoja 1')
        hoja_1.write(0, 0, "Caudal (Q)")
        hoja_1.write(0, 1, Caudal)
        hoja_1.write(1, 0, "Espejo agua (b)")
        hoja_1.write(1, 1, Espejo_agua)
        hoja_1.write(2, 0, "Coef_friccion (z)")
        hoja_1.write(2, 1, Coef_friccion)

        hoja_1.write(0, 3, "Tirante Crítico (y)")
        hoja_1.write(0, 4, tirante_critico)
        hoja_1.write(1, 3, "Área hidráulica (A)")
        hoja_1.write(1, 4, area)
        hoja_1.write(2, 3, "Foco parábola")
        hoja_1.write(2, 4, foco_parabola)
        hoja_1.write(3, 3, "Número de Froude")
        hoja_1.write(3, 4, numero_froude)
        hoja_1.write(4, 3, "Pendiente hidráulica")
        hoja_1.write(4, 4, pendiente_hidraulica)
        hoja_1.write(5, 3, "Perímetro")
        hoja_1.write(5, 4, perimetro)
        hoja_1.write(6, 3, "Radio hidráulico")
        hoja_1.write(6, 4, radio_hidraulico)
        hoja_1.write(7, 3, "Velocidad")
        hoja_1.write(7, 4, velocidad)
        hoja_1.write(8, 3, "Energía Específica")
        hoja_1.write(8, 4, energia_especifica)

        # cambiando tamaño a las columnas
        col_1 = hoja_1.col(0)
        col_1.width = 5500
        col_2 = hoja_1.col(1)
        col_2.width = 2300

        col_4 = hoja_1.col(3)
        col_4.width = 4500
        col_5 = hoja_1.col(4)
        col_5.width = 2300

        wb.save('canal_parabolico.xls')

        print('exportar excel')

    def exportar_pdf(self):
        Caudal = self.caudal_entry.get()
        Espejo_agua = self.espejo_agua_entry.get()
        Coef_friccion = self.coef_friccion_entry.get()
        tirante_critico = self.tirante_critico_entry.cget("text")
        area = self.area_entry.cget("text")
        foco_parabola = self.foco_parabola_entry.cget("text")
        numero_froude = self.numero_froude_entry.cget("text")
        pendiente_hidraulica = self.pendiente_hidraulica_entry.cget("text")
        perimetro = self.perimetro_entry.cget("text")
        radio_hidraulico = self.radio_hidraulico_entry.cget("text")
        velocidad = self.velocidad_entry.cget("text")
        energia_especifica = self.energia_especifica_entry.cget("text")
        pdf = fpdf.FPDF()
        # añadiendo una pag al pdf
        pdf.add_page()
        title = 'Cálculo de Canal Parabólico'

        pdf.set_xy(0.0, 0.0)
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(w=210.0, h=40.0, align='C', txt=title, border=0)

        pdf.set_font('Arial', '', 10)

        # añadiendo celdas al pdf
        pdf.set_xy(20.0, 30.0)
        pdf.cell(w=55.0, h=10.0, align='L', txt="Caudal (Q)", border=1)
        pdf.set_xy(75.0, 30.0)
        pdf.cell(w=15.0, h=10.0, align='L', txt=Caudal, border=1)
        pdf.set_xy(20.0, 40.0)
        pdf.cell(w=55.0, h=10.0, align='L', txt="Espejo agua (b)", border=1)
        pdf.set_xy(75.0, 40.0)
        pdf.cell(w=15.0, h=10.0, align='L', txt=Espejo_agua, border=1)
        pdf.set_xy(20.0, 50.0)
        pdf.cell(w=55.0, h=10.0, align='L', txt="Coef_friccion (z)", border=1)
        pdf.set_xy(75.0, 50.0)
        pdf.cell(w=15.0, h=10.0, align='L', txt=Coef_friccion, border=1)

        pdf.set_xy(90.0, 30.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Tirante Critico (y)", border=1)
        pdf.set_xy(140.0, 30.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=tirante_critico, border=1)
        pdf.set_xy(90.0, 40.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Area hidráulica (A)", border=1)
        pdf.set_xy(140.0, 40.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=area, border=1)
        pdf.set_xy(90.0, 50.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Foco Parabólico", border=1)
        pdf.set_xy(140.0, 50.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=foco_parabola, border=1)
        pdf.set_xy(90.0, 60.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Número de Froude", border=1)
        pdf.set_xy(140.0, 60.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=numero_froude, border=1)
        pdf.set_xy(90.0, 70.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Pendiente hidráulica", border=1)
        pdf.set_xy(140.0, 70.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=pendiente_hidraulica, border=1)
        pdf.set_xy(90.0, 80.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Perímetro", border=1)
        pdf.set_xy(140.0, 80.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=perimetro, border=1)
        pdf.set_xy(90.0, 90.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Radio hidráulico", border=1)
        pdf.set_xy(140.0, 90.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=radio_hidraulico, border=1)
        pdf.set_xy(90.0, 100.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Velocidad", border=1)
        pdf.set_xy(140.0, 100.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=velocidad, border=1)
        pdf.set_xy(90.0, 110.0)
        pdf.cell(w=50.0, h=10.0, align='L', txt="Energía Especifica (E)", border=1)
        pdf.set_xy(140.0, 110.0)
        pdf.cell(w=60.0, h=10.0, align='L', txt=energia_especifica, border=1)

        pdf.output('canal_parabolico.pdf', 'F')

        print('exportar pdf')

    def cambio_unidades(self):
        self.internacional = not self.internacional
        if self.internacional:
            self.caudal_label.config(text="m3/s")
            self.espejo_agua_label.config(text="m")
            self.coef_friccion_entry.config(text="")

            self.tirante_critico_label.config(text="m")
            self.area_label.config(text="m2")
            self.foco_parabola_label.config(text="m")
            self.numero_froude_label.config(text="")
            self.pendiente_hidraulica_label.config(text="")
            self.perimetro_label.config(text="m")
            self.radio_hidraulico_label.config(text="m")
            self.velocidad_label.config(text="m/s")
            self.energia_especifica_label.config(text="m-Kg/Kg")

        else:
            self.caudal_label.config(text="ft3/s")
            self.espejo_agua_label.config(text="ft")
            self.coef_friccion_entry.config(text="")

            self.tirante_critico_label.config(text="ft")
            self.area_label.config(text="ft2")
            self.foco_parabola_label.config(text="ft")
            self.numero_froude_label.config(text="")
            self.pendiente_hidraulica_label.config(text="")
            self.perimetro_label.config(text="ft")
            self.radio_hidraulico_label.config(text="ft")
            self.velocidad_label.config(text="ft/s")
            self.energia_especifica_label.config(text="ft-Kg/Kg")

        print('cambio unidades')
