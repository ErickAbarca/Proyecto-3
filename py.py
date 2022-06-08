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

        self.btn_1 = Button(self, text="Ingresar")
        self.btn_1.place(x=100, y=100)

        self.btn_2 = Button(self, text="Consultar")
        self.btn_2.place(x=100, y=150)

        self.btn_3 = Button(self, text="Eliminar")
        self.btn_3.place(x=100, y=200)

        self.btn_4 = Button(self, text="Salir")
        self.btn_4.place(x=200, y=100)
        
        self.btn_5 = Button(self, text="Salir")
        self.btn_5.place(x=200, y=150)

        self.btn_6 = Button(self, text="Salir")
        self.btn_6.place(x=200, y=200)
        
menu_principal().mainloop()