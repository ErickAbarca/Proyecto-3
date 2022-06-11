'''
3 Proyecto de programación

Taller de programación

Estudiante: Erick Abarca Calderon

Profesor: William Mata Rodriguez
'''

from tkinter import *
import tkinter

class menu_principal(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("400x400")
        self.title("Menu Principal")
        self.configure(bg="white")
        self.iconbitmap('icon.ico')

        altura=3
        
        self.btn_1 = Button(self, text="Configuración",height=altura)
        self.btn_1.place(x=100, y=100)

        self.btn_2 = Button(self, text="Cargar Cajero",height=altura)
        self.btn_2.place(x=100, y=150)

        self.btn_3 = Button(self, text="Saldo del Cajero",height=altura)
        self.btn_3.place(x=100, y=200)

        self.btn_4 = Button(self, text="Ingresos de dinero",height=altura)
        self.btn_4.place(x=200, y=100)
        
        self.btn_5 = Button(self, text="Entrada de vehículo",height=altura)
        self.btn_5.place(x=200, y=150)

        self.btn_6 = Button(self, text="Cajero del Parqueo",height=altura)
        self.btn_6.place(x=200, y=200)

        self.btn_7 = Button(self, text="Cajero del Parqueo",height=altura)
        self.btn_7.place(x=100, y=250)

        self.btn_6 = Button(self, text="Cajero del Parqueo",height=altura)
        self.btn_6.place(x=200, y=200)
        
menu_principal().mainloop()