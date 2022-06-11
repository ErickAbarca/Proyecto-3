'''
3 Proyecto de programación

Taller de programación

Estudiante: Erick Abarca Calderon

Profesor: William Mata Rodriguez
'''

from tkinter import *
import tkinter
from pickle import *


class menu_principal(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("550x400")
        self.title("Menu Principal")
        self.configure(bg="white")
        self.iconbitmap('icon.ico')

        altura=3
        ancho=20
        posx1=75
        posx2=300
        tmn_font=12

        self.lbl_titulo = Label(self, text="Menu Principal", font=("Arial", 20), bg="white")
        self.lbl_titulo.place(x=175)
        
        self.btn_1 = Button(self, text="Configuración",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_1.place(x=posx1, y=50)

        self.btn_2 = Button(self, text="Cargar Cajero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_2.place(x=posx1, y=125)

        self.btn_3 = Button(self, text="Saldo del Cajero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_3.place(x=posx1, y=200)

        self.btn_4 = Button(self, text="Ingresos de dinero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_4.place(x=posx2, y=50)
        
        self.btn_5 = Button(self, text="Entrada de vehículo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_5.place(x=posx2, y=125)

        self.btn_6 = Button(self, text="Cajero del Parqueo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_6.place(x=posx2, y=200)

        self.btn_7 = Button(self, text="Salida de vehiculo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_7.place(x=posx1, y=275)

        self.btn_6 = Button(self, text="Ayuda",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_6.place(x=posx2, y=275)

class configuracion(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("550x400")
        self.title("Parqueo-Configuración")
        self.configure(bg="white")
        self.iconbitmap('settings.ico')

        f=open('configuracion.dat','r')
        lines=f.readlines()
        f.close()

        conf=[]
        for line in lines:
            conf.append(eval(line[:-1]))


configuracion().mainloop()