'''
3 Proyecto de programación

Taller de programación

Estudiante: Erick Abarca Calderon

Profesor: William Mata Rodriguez
'''

from tkinter import *
import tkinter
from tkinter import messagebox
from pickle import *
from validate_email import validate_email
from datetime import datetime
import os


class menu_principal(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("550x400")
        self.title("Menu Principal")
        self.configure(bg="white")
        self.iconbitmap('icon.ico')
        self.resizable(False, False)

        #variables de ubicacion de los botones
        altura=3
        ancho=20
        posx1=75
        posx2=300
        tmn_font=12

        #Creacion de los botones y colocacion de los mismos
        self.lbl_titulo = Label(self, text="Menu Principal", font=("Arial", 20), bg="white")
        self.lbl_titulo.place(x=175)
        
        self.btn_1 = Button(self, text="Configuración",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.abrir_configuracion)
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

        self.btn_6 = Button(self, text="Ayuda",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.abrir_ayuda)
        self.btn_6.place(x=posx2, y=275)

    def abrir_configuracion(self):
        self.destroy()
        self.configuracion = configuracion()
        self.configuracion.mainloop()

    def abrir_ayuda(self):
        os.startfile('p3.pdf')
class configuracion(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("600x600")
        self.title("Parqueo-Configuración")
        self.configure(bg="white")
        self.iconbitmap('settings.ico')
        self.resizable(False, False)

       

        sub_res=[]
        posxlab=0
        posxent=500
        fo=('Arial',12)
        #Se crean los labels y los entrys
        self.lbl_titulo = Label(self, text="Configuración", font=("Arial", 20), bg="white")
        self.lbl_titulo.place(x=175)

        self.lbl_1 = Label(self, text="Cantidad de espacios en el parqueo:", font=fo, bg="white")
        self.lbl_1.place(x=posxlab, y=50)
        self.esp = Entry(self, width=5, font=fo,relief='solid')
        self.esp.place(x=posxent, y=50)

        self.lbl_2 = Label(self, text="Precio por hora:", font=fo, bg="white")
        self.lbl_2.place(x=posxlab, y=80)
        self.pph = Entry(self, width=5, font=fo,relief='solid')
        self.pph.place(x=posxent, y=80)

        self.lbl_3 = Label(self, text="Pago mínimo", font=fo, bg="white")
        self.lbl_3.place(x=posxlab, y=110)
        self.pag_min = Entry(self, width=5, font=fo,relief='solid')
        self.pag_min.place(x=posxent, y=110)

        self.lbl_4 = Label(self, text="Correo electrónico del supervisor", font=fo, bg="white")
        self.lbl_4.place(x=posxlab, y=140)
        self.correo = Entry(self, width=20, font=fo,relief='solid')
        self.correo.place(x=365, y=140)

        self.lbl_5 = Label(self, text="Minutos máximos para salir después del pago", font=fo, bg="white")
        self.lbl_5.place(x=posxlab, y=170)
        self.minsmax = Entry(self, width=5, font=fo,relief='solid')
        self.minsmax.place(x=posxent, y=170)

        self.lbl51=Label(self,text="Denominación de monedas, máximo 3",font=fo,bg="white")
        self.lbl51.place(x=posxlab,y=210)

        self.lbl_6 = Label(self, text="Moneda 1", font=fo, bg="white")
        self.lbl_6.place(x=posxlab, y=230)
        self.m1 = Entry(self, width=5, font=fo,relief='solid')
        self.m1.place(x=posxent, y=230)

        self.lbl_7 = Label(self, text="Moneda 2", font=fo, bg="white")
        self.lbl_7.place(x=posxlab, y=260)
        self.m2 = Entry(self, width=5, font=fo,relief='solid')
        self.m2.place(x=posxent, y=260)

        self.lbl_8 = Label(self, text="Moneda 3", font=fo, bg="white")
        self.lbl_8.place(x=posxlab, y=290)
        self.m3 = Entry(self, width=5, font=fo,relief='solid')
        self.m3.place(x=posxent, y=290)

        self.lbl81=Label(self,text="Denominación de billetes, máximo 5",font=fo,bg="white")
        self.lbl81.place(x=posxlab,y=330)

        self.lbl_9 = Label(self, text="Billete 1", font=fo, bg="white")
        self.lbl_9.place(x=posxlab, y=350)
        self.b1 = Entry(self, width=5, font=fo,relief='solid')
        self.b1.place(x=posxent, y=350)

        self.lbl_10 = Label(self, text="Billete 2", font=fo, bg="white")
        self.lbl_10.place(x=posxlab, y=380)
        self.b2 = Entry(self, width=5, font=fo,relief='solid')
        self.b2.place(x=posxent, y=380)

        self.lbl_11 = Label(self, text="Billete 3", font=fo, bg="white")
        self.lbl_11.place(x=posxlab, y=410)
        self.b3 = Entry(self, width=5, font=fo,relief='solid')
        self.b3.place(x=posxent, y=410)

        self.lbl_12 = Label(self, text="Billete 4", font=fo, bg="white")
        self.lbl_12.place(x=posxlab, y=440)
        self.b4 = Entry(self, width=5, font=fo,relief='solid')
        self.b4.place(x=posxent, y=440)

        self.lbl_13 = Label(self, text="Billete 5", font=fo, bg="white")
        self.lbl_13.place(x=posxlab, y=470)
        self.b5 = Entry(self, width=5, font=fo,relief='solid')
        self.b5.place(x=posxent, y=470)

        self.confirmar = Button(self, text="Confirmar", font=fo,bg='blue2',fg='white',command=lambda:self.guardar())
        self.confirmar.place(x=175, y=500)

        self.cancelar = Button(self, text="Cancelar", font=fo, bg='blue2',fg='white',command=lambda:self.salir())
        self.cancelar.place(x=275, y=500)

    def guardar(self):

        subres=[]
        monedas=[5,10,25,50,100,500]
        billetes=[1000,2000,5000,10000,20000]

        self.espacios = self.esp.get()
        if self.espacios=='':
            subres.append(0)
        else:
            try :
                self.espacios = int(self.espacios)
                if self.espacios < 1:
                    messagebox.showerror("Error", "La cantidad de espacios debe ser mayor a 0")
                subres.append(self.espacios)
            except ValueError:
                messagebox.showerror("Error", "La cantidad de espacios debe ser un número")

        self.pphora = self.pph.get()
        if self.pphora=='':
            subres.append(0)
        else:
            try :
                self.pphora = int(self.pphora)
                if self.pphora < 1:
                    messagebox.showerror("Error", "El pago por hora debe ser mayor a 0")
                subres.append(self.pphora)
            except ValueError:
                messagebox.showerror("Error", "El pago por hora debe ser un número")

        self.pago_min = self.pag_min.get()
        if self.pago_min=='':
            subres.append(0)
        else:
            try :
                self.pago_min = int(self.pago_min)
                if self.pago_min < 1:
                    messagebox.showerror("Error", "El pago mínimo debe ser mayor a 0")
                subres.append(self.pago_min)
            except ValueError:
                messagebox.showerror("Error", "El pago mínimo debe ser un número")

        self.email = self.correo.get()
        if self.email=='':
            subres.append('')
        else:
            if validate_email(self.email)==False:
                messagebox.showerror("Error", "El correo no es válido")
            else:
                subres.append(self.email)
        
        self.minsmaximo = self.minsmax.get()
        if self.minsmaximo=='':
            subres.append(0)
        else:
            try :
                self.minsmaximo = int(self.minsmaximo)
                if self.minsmaximo < 0:
                    messagebox.showerror("Error", "El máximo de minutos debe ser mayor a 0")
                subres.append(datetime.strptime(str(self.minsmaximo), '%M'))
            except ValueError:
                messagebox.showerror("Error", "El máximo de minutos debe ser un número")
        
        self.moneda1 = self.m1.get()
        if self.moneda1=='':
            subres.append(0)
        else:
            try :
                self.moneda1 = int(self.moneda1)
                if self.moneda1 not in monedas:
                    messagebox.showerror("Error", "La moneda 1 debe ser una de las siguientes denominaciones: 5,10,25,50,100,500")
                else:
                    subres.append(self.moneda1)
            except ValueError:
                messagebox.showerror("Error", "La denominación de moneda 1 debe ser un número")


        self.moneda2 = self.m2.get()
        if self.moneda2=='':
            subres.append(0)
        else:
            try :
                self.moneda2 = int(self.moneda2)
                if self.moneda2 not in monedas:
                    messagebox.showerror("Error", "La denominación de moneda 2 no existe")
                else:
                    i = monedas.index(self.moneda1)
                    if self.moneda2 == monedas[i+1]: 
                        subres.append(self.moneda2)
                    else:
                        messagebox.showerror("Error", "La denominación de moneda 2 debe ser la siguiente a la denominación de moneda 1")
            except ValueError:
                messagebox.showerror("Error", "La denominación de moneda 2 debe ser un número")

        self.moneda3 = self.m3.get()
        if self.moneda3=='':
            subres.append(0)
        else:
            try :
                self.moneda3 = int(self.moneda3)
                if self.moneda3 not in monedas:
                    messagebox.showerror("Error", "La denominación de moneda 3 no existe")
                else:
                    i = monedas.index(self.moneda2)
                    if self.moneda3 == monedas[i+1]: 
                        subres.append(self.moneda3)
                    else:
                        messagebox.showerror("Error", "La denominación de moneda 3 debe ser la siguiente a la denominación de moneda 2")
            except ValueError:
                messagebox.showerror("Error", "La denominación de moneda 3 debe ser un número")
        
        self.billete1 = self.b1.get()
        if self.billete1=='':
            subres.append(0)
        else:
            try :
                self.billete1 = int(self.billete1)
                if self.billete1 not in billetes:
                    messagebox.showerror("Error", "La denominación de billete 1 no existe")
                else:
                    subres.append(self.billete1)
            except ValueError:
                messagebox.showerror("Error", "La denominación de billete 1 debe ser un número")
        
        self.billete2 = self.b2.get()
        if self.billete2=='':
            subres.append(0)
        else:
            try :
                self.billete2 = int(self.billete2)
                if self.billete2 not in billetes:
                    messagebox.showerror("Error", "La denominación de billete 2 no existe")
                else:
                    i = billetes.index(self.billete1)
                    if self.billete2 == billetes[i+1]: 
                        subres.append(self.billete2)
                    else:
                        messagebox.showerror("Error", "La denominación de billete 2 debe ser la siguiente a la denominación de billete 1")
            except ValueError:
                messagebox.showerror("Error", "La denominación de billete 2 debe ser un número")
        

        self.billete3 = self.b3.get()
        if self.billete3=='':
            subres.append(0)
        else:
            try :
                self.billete3 = int(self.billete3)
                if self.billete3 not in billetes:
                    messagebox.showerror("Error", "La denominación de billete 3 no existe")
                else:
                    i = billetes.index(self.billete2)
                    if self.billete3 == billetes[i+1]: 
                        subres.append(self.billete3)
                    else:
                        messagebox.showerror("Error", "La denominación de billete 3 debe ser la siguiente a la denominación de billete 2")
            except ValueError:
                messagebox.showerror("Error", "La denominación de billete 3 debe ser un número")
        
        self.billete4 = self.b4.get()
        if self.billete4=='':
            subres.append(0)
        else:
            try :
                self.billete4 = int(self.billete4)
                if self.billete4 not in billetes:
                    messagebox.showerror("Error", "La denominación de billete 4 no existe")
                else:
                    i = billetes.index(self.billete3)
                    if self.billete4 == billetes[i+1]: 
                        subres.append(self.billete4)
                    else:
                        messagebox.showerror("Error", "La denominación de billete 4 debe ser la siguiente a la denominación de billete 3")
            except ValueError:
                messagebox.showerror("Error", "La denominación de billete 4 debe ser un número")
        
        self.billete5 = self.b5.get()
        if self.billete5=='':
            subres.append(0)
        else:
            try :
                self.billete5 = int(self.billete5)
                if self.billete5 not in billetes:
                    messagebox.showerror("Error", "La denominación de billete 5 no existe")
                else:
                    i = billetes.index(self.billete4)
                    if self.billete5 == billetes[i+1]: 
                        subres.append(self.billete5)
                    else:
                        messagebox.showerror("Error", "La denominación de billete 5 debe ser la siguiente a la denominación de billete 4")
            except ValueError:
                messagebox.showerror("Error", "La denominación de billete 5 debe ser un número")
        
        #Se abre el archivo de configuracion y se lee el contenido
        f=open('configuracion.dat','r')
        line=f.read()
        f.close()
        conf=eval(line)

        g=[]
        #Se comparan las listas y se crea una nueva lista con los nuevos valores
        for n_i,i in enumerate(conf):
            if subres[n_i]==0 or subres[n_i]=='':
                g.append(str(i))
            else:
                if i!=subres[n_i]:
                   g.append(str(subres[n_i]))
                else:
                   g.append(str(i))
        
        print(g)
        #se crea un mensaje para confirmar la configuracion
        ask= messagebox.askquestion("Confirmar", "¿Está seguro de que desea guardar la configuración?")
        if ask=='yes':
            f=open('configuracion.dat','w')
            f.write(str(g))
            f.close()
            messagebox.showinfo("Confirmación", "Configuración guardada")
            self.destroy()
            self.principal=menu_principal()
            self.principal.mainloop()
        else:
            messagebox.showinfo("Atención", "La configuración no se ha guardado")

    def salir(self):
        self.destroy()
        self.principal=menu_principal()
        self.principal.mainloop()

class cargar_cajero(tkinter.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Parqueo-Cargar Cajero")
        self.geometry("300x200")
        self.resizable(False, False)
        self.config(bg='white')
        self.iconbitmap('dolar.ico')

        self.l1 = tkinter.Label(self, text="Cargar cajero", font=("Arial", 20), bg='white')
        self.l1.place(x=100, y=10)




configuracion().mainloop()