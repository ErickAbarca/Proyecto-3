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
import datetime
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

        self.btn_2 = Button(self, text="Cargar Cajero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.abrir_cargar_cajero)
        self.btn_2.place(x=posx1, y=125)

        self.btn_3 = Button(self, text="Saldo del Cajero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_3.place(x=posx1, y=200)

        self.btn_4 = Button(self, text="Ingresos de dinero",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font))
        self.btn_4.place(x=posx2, y=50)
        
        self.btn_5 = Button(self, text="Entrada de vehículo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.entrada_de_vehiculo)
        self.btn_5.place(x=posx2, y=125)

        self.btn_6 = Button(self, text="Cajero del Parqueo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.cajero_del_parqueo)
        self.btn_6.place(x=posx2, y=200)

        self.btn_7 = Button(self, text="Salida de vehiculo",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.salida_de_vehiculo)
        self.btn_7.place(x=posx1, y=275)

        self.btn_6 = Button(self, text="Ayuda",height=altura,width=ancho,bg='blue2',fg='white',font=('Arial Nova',tmn_font),command=self.abrir_ayuda)
        self.btn_6.place(x=posx2, y=275)

    def abrir_configuracion(self):
        self.destroy()
        self.configuracion = configuracion()
        self.configuracion.mainloop()
    
    def abrir_cargar_cajero(self):
        self.destroy()
        self.cargar_cajero = cargar_cajero()
        self.cargar_cajero.mainloop()

    def entrada_de_vehiculo(self):
        self.destroy()
        self.entrada_de_vehiculo = entrada_de_vehiculo()
        self.entrada_de_vehiculo.mainloop()

    def cajero_del_parqueo(self):
        self.destroy()
        self.cajero_del_parqueo = cajero_del_parqueo()
        self.cajero_del_parqueo.mainloop()

    def salida_de_vehiculo(self):
        self.destroy()
        self.salida_de_vehiculo = salida_de_vehiculo()
        self.salida_de_vehiculo.mainloop()

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
                fk=open('parqueo.dat','r')
                parqueo=fk.read()
                fk.close()
                parqueo=eval(parqueo)
                if len (parqueo)>0:
                    messagebox.showerror("Error","Existen vehiculos en el parqueo")
                    return
                else:
                    if self.espacios < 1:
                        messagebox.showerror("Error", "La cantidad de espacios debe ser mayor a 0")
                        return
                    subres.append(self.espacios)        
            except ValueError:
                messagebox.showerror("Error", "La cantidad de espacios debe ser un número")
                return

        self.pphora = self.pph.get()
        if self.pphora=='':
            subres.append(0)
        else:
            try :
                self.pphora = int(self.pphora)
                if self.pphora < 1:
                    messagebox.showerror("Error", "El pago por hora debe ser mayor a 0")
                    return
                subres.append(self.pphora)
            except ValueError:
                messagebox.showerror("Error", "El pago por hora debe ser un número")
                return

        self.pago_min = self.pag_min.get()
        if self.pago_min=='':
            subres.append(0)
        else:
            try :
                self.pago_min = int(self.pago_min)
                if self.pago_min < 1:
                    messagebox.showerror("Error", "El pago mínimo debe ser mayor a 0")
                    return
                subres.append(self.pago_min)
            except ValueError:
                messagebox.showerror("Error", "El pago mínimo debe ser un número")
                return

        self.email = self.correo.get()
        if self.email=='':
            subres.append('')
        else:
            if validate_email(self.email)==False:
                messagebox.showerror("Error", "El correo no es válido")
                return
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
                    return
                subres.append(self.minsmaximo)
            except ValueError:
                messagebox.showerror("Error", "El máximo de minutos debe ser un número")
                return
        
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
                g.append(i)
            else:
                if i!=subres[n_i]:
                   g.append(subres[n_i])
                else:
                   g.append(i)
        
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

        fo=("Arial", 12)
        fila1=50
        fila2=80
        fila3=110
        fila4=140
        fila5=170
        fila6=200
        fila7=240
        fila8=270
        fila9=300
        fila10=330
        fila11=360
        fila12=390
        fila13=430
        fila14=470

        col1=10
        col2=230
        col3=310
        col4=475
        col5=605
        col6=725
        col7=810

        f=open('configuracion.dat','r')
        line=f.read()
        f.close()
        conf=eval(line)

        self.txtmoneda1=str(conf[5])
        self.txtmoneda2=str(conf[6])
        self.txtmoneda3=str(conf[7])
        self.txtbillet1=str(conf[8])
        self.txtbillet2=str(conf[9])
        self.txtbillet3=str(conf[10])
        self.txtbillet4=str(conf[11])
        self.txtbillet5=str(conf[12])

        fi=open('cajero.dat','r')
        salact=fi.read()
        fi.close()
        salact=eval(salact)

        self.cantmoneda1=salact[0]
        self.cantmoneda2=salact[1]
        self.cantmoneda3=salact[2]
        self.cantbillet1=salact[3]
        self.cantbillet2=salact[4]
        self.cantbillet3=salact[5]
        self.cantbillet4=salact[6]
        self.cantbillet5=salact[7]

        #Variables que se usan para guardar los valores de las cajas de texto
        self.total_mon_antes=self.cantmoneda1+self.cantmoneda2+self.cantmoneda3
        self.total_bil_antes=self.cantbillet1+self.cantbillet2+self.cantbillet3+self.cantbillet4+self.cantbillet5
        self.total_cant_car_mon=0
        self.total_cant_car_bil=0
        self.tot_din_car_mon=0
        self.tot_din_car_bil=0
        self.tot_can_fin_mon=0
        self.tot_can_fin_bil=0

        #Variables que se usan para guardar los valores en el arvhivo al final
        self.subres=[self.cantmoneda1,self.cantmoneda2,self.cantmoneda3,self.cantbillet1,self.cantbillet2,self.cantbillet3,self.cantbillet4,self.cantbillet5]


        self.title("Parqueo-Cargar Cajero")
        self.geometry("900x550")
        self.resizable(False, False)
        self.config(bg='white')
        self.iconbitmap('dolar.ico')

        self.l1 = tkinter.Label(self, text="Cargar cajero", font=("Arial", 20), bg='white')
        self.l1.place(x=350, y=10)

        self.l2 = tkinter.Label(self, text="Denominación", font=fo, bg='white')
        self.l2.place(x=10, y=fila2)

        self.l3 = tkinter.Label(self, text="Saldo antes de la carga", font=fo, bg='white')
        self.l3.place(x=200, y=fila1)

        self.l4 = tkinter.Label(self, text="Carga", font=fo, bg='white')
        self.l4.place(x=550, y=fila1)

        self.l5 = tkinter.Label(self, text="Saldo", font=fo, bg='white')
        self.l5.place(x=750, y=fila1)

        self.l6 = tkinter.Label(self, text="Cantidad", font=fo, bg='white')
        self.l6.place(x=200, y=fila2)

        self.l7 = tkinter.Label(self, text="Total", font=fo, bg='white')
        self.l7.place(x=300, y=fila2)

        self.l8 = tkinter.Label(self, text="Cantidad", font=fo, bg='white')
        self.l8.place(x=500, y=fila2)

        self.l9 = tkinter.Label(self, text="Total", font=fo, bg='white')
        self.l9.place(x=600, y=fila2)

        self.l10 = tkinter.Label(self, text="Cantidad", font=fo, bg='white')
        self.l10.place(x=700, y=fila2)

        self.l11 = tkinter.Label(self, text="Total", font=fo, bg='white')
        self.l11.place(x=800, y=fila2)

        ##############
        #Moneda 1
        ##############

        self.l12 = tkinter.Label(self, text='Monedas de '+str(self.txtmoneda1), font=fo, bg='white')
        self.l12.place(x=col1, y=fila3)

        self.l13 = tkinter.Label(self, text=self.cantmoneda1, font=fo, bg='white')
        self.l13.place(x=col2, y=fila3)

        self.totalm1=int(self.cantmoneda1)*int(self.txtmoneda1)

        self.l14 = tkinter.Label(self, text=str(self.totalm1), font=fo, bg='white')
        self.l14.place(x=col3, y=fila3)
        
        self.ent_m1=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_m1.place(x=col4, y=fila3)
        
        self.total_carga_m1 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_m1.place(x=col5, y=fila3)

        self.cant_tot_m1 = tkinter.Label(self, text=self.cantmoneda1, font=fo, bg='white')
        self.cant_tot_m1.place(x=col6, y=fila3)

        self.tot_fin_m1 = tkinter.Label(self, text=str(self.totalm1), font=fo, bg='white')
        self.tot_fin_m1.place(x=col7, y=fila3)

        self.ent_m1.bind("<KeyRelease>", self.cargar_m1)

        #################
        #Moneda 2
        #################

        self.l15 = tkinter.Label(self, text='Monedas de '+self.txtmoneda2, font=fo, bg='white')
        self.l15.place(x=col1, y=fila4)

        self.l16 = tkinter.Label(self, text=self.cantmoneda2, font=fo, bg='white')
        self.l16.place(x=col2, y=fila4)

        self.totalm2=int(self.cantmoneda2)*int(self.txtmoneda2)

        self.l17 = tkinter.Label(self, text=str(self.totalm2), font=fo, bg='white')
        self.l17.place(x=col3, y=fila4)

        self.ent_m2=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_m2.place(x=col4, y=fila4)

        self.total_carga_m2 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_m2.place(x=col5, y=fila4)

        self.cant_tot_m2 = tkinter.Label(self, text=self.cantmoneda2, font=fo, bg='white')
        self.cant_tot_m2.place(x=col6, y=fila4)

        self.tot_fin_m2 = tkinter.Label(self, text=str(self.totalm2), font=fo, bg='white')
        self.tot_fin_m2.place(x=col7, y=fila4)

        self.ent_m2.bind("<KeyRelease>", self.cargar_m2)

        #################
        #Moneda 3
        #################

        self.l18 = tkinter.Label(self, text='Monedas de '+self.txtmoneda3, font=fo, bg='white')
        self.l18.place(x=col1, y=fila5)

        self.l19 = tkinter.Label(self, text=self.cantmoneda3, font=fo, bg='white')
        self.l19.place(x=col2, y=fila5)

        self.totalm3=int(self.cantmoneda3)*int(self.txtmoneda3)

        self.l20 = tkinter.Label(self, text=str(self.totalm3), font=fo, bg='white')
        self.l20.place(x=col3, y=fila5)

        self.ent_m3=Entry(self, width=10,font=fo, bg='white',relief='solid')
        self.ent_m3.place(x=col4, y=fila5)

        self.total_carga_m3 = tkinter.Label(self,text=0 ,font=fo, bg='white')
        self.total_carga_m3.place(x=col5, y=fila5)

        self.cant_tot_m3 = tkinter.Label(self, text=self.cantmoneda3, font=fo, bg='white')
        self.cant_tot_m3.place(x=col6, y=fila5)

        self.tot_fin_m3 = tkinter.Label(self, text=str(self.totalm3), font=fo, bg='white')
        self.tot_fin_m3.place(x=col7, y=fila5)

        self.ent_m3.bind("<KeyRelease>", self.cargar_m3)

        
        #################
        #Total de monedas
        #################

        self.l21 = tkinter.Label(self, text='Total de monedas', font=fo, bg='white')
        self.l21.place(x=col1, y=fila6)

        self.l22 = tkinter.Label(self, text=self.total_mon_antes, font=fo, bg='white')
        self.l22.place(x=col2, y=fila6)

        self.l23 = tkinter.Label(self, text=(self.totalm1+self.totalm2+self.totalm3), font=fo, bg='white')
        self.l23.place(x=col3, y=fila6)

        self.tot_cant_car_m = tkinter.Label(self, text=0, font=fo, bg='white')
        self.tot_cant_car_m.place(x=col4, y=fila6)

        self.tot_carg_tot_m = tkinter.Label(self, text=0, font=fo, bg='white')
        self.tot_carg_tot_m.place(x=col5, y=fila6)

        self.sald_cant_tot_m = tkinter.Label(self, text=str(int(self.cant_tot_m1.cget('text'))+int(self.cant_tot_m2.cget('text'))+int(self.cant_tot_m3.cget('text'))), font=fo, bg='white')
        self.sald_cant_tot_m.place(x=col6, y=fila6)

        self.sald_tot_m = tkinter.Label(self, text=str(int(self.tot_fin_m1.cget('text'))+int(self.tot_fin_m2.cget('text'))+int(self.tot_fin_m3.cget('text'))), font=fo, bg='white')
        self.sald_tot_m.place(x=col7, y=fila6)

        #################
        #Billete 1
        #################

        self.l24 = tkinter.Label(self, text='Billetes de '+self.txtbillet1, font=fo, bg='white')
        self.l24.place(x=col1, y=fila7)

        self.l25 = tkinter.Label(self, text=self.cantbillet1, font=fo, bg='white')
        self.l25.place(x=col2, y=fila7)

        self.totalb1=int(self.cantbillet1)*int(self.txtbillet1)
        
        self.l26 = tkinter.Label(self, text=str(self.totalb1), font=fo, bg='white')
        self.l26.place(x=col3, y=fila7)

        self.ent_b1=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_b1.place(x=col4, y=fila7)

        self.total_carga_b1 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_b1.place(x=col5, y=fila7)

        self.cant_tot_b1 = tkinter.Label(self, text=self.cantbillet1, font=fo, bg='white')
        self.cant_tot_b1.place(x=col6, y=fila7)

        self.tot_fin_b1 = tkinter.Label(self, text=str(self.totalb1), font=fo, bg='white')
        self.tot_fin_b1.place(x=col7, y=fila7)

        self.ent_b1.bind("<KeyRelease>", self.cargar_b1)

        #################
        #Billete 2
        #################

        self.l27 = tkinter.Label(self, text='Billetes de '+self.txtbillet2, font=fo, bg='white')
        self.l27.place(x=col1, y=fila8)

        self.l28 = tkinter.Label(self, text=self.cantbillet2, font=fo, bg='white')
        self.l28.place(x=col2, y=fila8)

        self.totalb2=int(self.cantbillet2)*int(self.txtbillet2)

        self.l29 = tkinter.Label(self, text=str(self.totalb2), font=fo, bg='white')
        self.l29.place(x=col3, y=fila8)

        self.ent_b2=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_b2.place(x=col4, y=fila8)

        self.total_carga_b2 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_b2.place(x=col5, y=fila8)
        
        self.cant_tot_b2 = tkinter.Label(self, text=self.cantbillet2, font=fo, bg='white')
        self.cant_tot_b2.place(x=col6, y=fila8)

        self.tot_fin_b2 = tkinter.Label(self, text=str(self.totalb2), font=fo, bg='white')
        self.tot_fin_b2.place(x=col7, y=fila8)

        self.ent_b2.bind("<KeyRelease>", self.cargar_b2)

        #################
        #Billete 3
        #################

        self.l30 = tkinter.Label(self, text='Billetes de '+self.txtbillet3, font=fo, bg='white')
        self.l30.place(x=col1, y=fila9)

        self.l31 = tkinter.Label(self, text=self.cantbillet3, font=fo, bg='white')
        self.l31.place(x=col2, y=fila9)

        self.totalb3=int(self.cantbillet3)*int(self.txtbillet3)
        
        self.l32 = tkinter.Label(self, text=str(self.totalb3), font=fo, bg='white')
        self.l32.place(x=col3, y=fila9)

        self.ent_b3=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_b3.place(x=col4, y=fila9)

        self.total_carga_b3 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_b3.place(x=col5, y=fila9)

        self.cant_tot_b3 = tkinter.Label(self, text=self.cantbillet3, font=fo, bg='white')
        self.cant_tot_b3.place(x=col6, y=fila9)

        self.tot_fin_b3 = tkinter.Label(self, text=str(self.totalb3), font=fo, bg='white')
        self.tot_fin_b3.place(x=col7, y=fila9)

        self.ent_b3.bind("<KeyRelease>", self.cargar_b3)

        #################
        #Billete 4
        #################

        self.l33 = tkinter.Label(self, text='Billetes de '+self.txtbillet4, font=fo, bg='white')
        self.l33.place(x=col1, y=fila10)

        self.l34 = tkinter.Label(self, text=self.cantbillet4, font=fo, bg='white')
        self.l34.place(x=col2, y=fila10)

        self.totalb4=int(self.cantbillet4)*int(self.txtbillet4)
        
        self.l35 = tkinter.Label(self, text=str(self.totalb4), font=fo, bg='white')
        self.l35.place(x=col3, y=fila10)

        self.ent_b4=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_b4.place(x=col4, y=fila10)

        self.total_carga_b4 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_b4.place(x=col5, y=fila10)

        self.cant_tot_b4 = tkinter.Label(self, text=self.cantbillet4, font=fo, bg='white')
        self.cant_tot_b4.place(x=col6, y=fila10)

        self.tot_fin_b4 = tkinter.Label(self, text=str(self.totalb4), font=fo, bg='white')
        self.tot_fin_b4.place(x=col7, y=fila10)

        self.ent_b4.bind("<KeyRelease>", self.cargar_b4)

        #################
        #Billete 5
        #################

        self.l36 = tkinter.Label(self, text='Billetes de '+self.txtbillet5, font=fo, bg='white')
        self.l36.place(x=col1, y=fila11)

        self.l37 = tkinter.Label(self, text=self.cantbillet5, font=fo, bg='white')
        self.l37.place(x=col2, y=fila11)

        self.totalb5=int(self.cantbillet5)*int(self.txtbillet5)

        self.l38 = tkinter.Label(self, text=str(self.totalb5), font=fo, bg='white')
        self.l38.place(x=col3, y=fila11)

        self.ent_b5=Entry(self, width=10, font=fo, bg='white',relief='solid')
        self.ent_b5.place(x=col4, y=fila11)

        self.total_carga_b5 = tkinter.Label(self, text=0, font=fo, bg='white')
        self.total_carga_b5.place(x=col5, y=fila11)

        self.cant_tot_b5 = tkinter.Label(self, text=self.cantbillet5, font=fo, bg='white')
        self.cant_tot_b5.place(x=col6, y=fila11)

        self.tot_fin_b5 = tkinter.Label(self, text=str(self.totalb5), font=fo, bg='white')
        self.tot_fin_b5.place(x=col7, y=fila11)

        self.ent_b5.bind("<KeyRelease>", self.cargar_b5)

        #################
        #Total de Billetes
        #################

        self.l39 = tkinter.Label(self, text='Total de Billetes', font=fo, bg='white')
        self.l39.place(x=col1, y=fila12)

        self.l40 = tkinter.Label(self, text=self.total_bil_antes, font=fo, bg='white')
        self.l40.place(x=col2, y=fila12)

        self.l23 = tkinter.Label(self, text=(self.totalb1+self.totalb2+self.totalb3+self.totalb4+self.totalb5), font=fo, bg='white')
        self.l23.place(x=col3, y=fila12)

        self.tot_cant_car_b = tkinter.Label(self, text=0, font=fo, bg='white')
        self.tot_cant_car_b.place(x=col4, y=fila12)

        self.tot_carg_tot_b = tkinter.Label(self, text=0, font=fo, bg='white')
        self.tot_carg_tot_b.place(x=col5, y=fila12)

        self.sald_cant_tot_b = tkinter.Label(self, text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))), font=fo, bg='white')
        self.sald_cant_tot_b.place(x=col6, y=fila12)

        self.sald_tot_b = tkinter.Label(self, text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))), font=fo, bg='white')
        self.sald_tot_b.place(x=col7, y=fila12)
        
        #################
        #Total final
        #################

        self.l41 = tkinter.Label(self, text='Total del cajero', font=fo, bg='white')
        self.l41.place(x=col1, y=fila13)

        self.total_final=tkinter.Label(self, text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))), font=fo, bg='white')
        self.total_final.place(x=col7, y=fila13)

        #################
        #Botones
        #################

        altura=2
        ancho=15
        fx=('Arial Nova',11)

        self.b1 = tkinter.Button(self, text='Cargar',height=altura,width=ancho,bg='blue2',fg='white',font=fx,command=lambda:self.btn_guardar())
        self.b1.place(x=col2-50, y=fila14)

        self.b2 = tkinter.Button(self, text='Cancelar',height=altura,width=ancho,bg='blue2',fg='white',font=fx, command=lambda:self.btn_cancelar())
        self.b2.place(x=col2+150, y=fila14)

        self.b3 = tkinter.Button(self, text='Vaciar Cajero',height=altura,width=ancho,bg='blue2',fg='white',font=fx, command=lambda:self.btn_vaciar())
        self.b3.place(x=col2+350, y=fila14)

    ##############################
    #Funciones de Cargar monedas
    ##############################
    def cargar_m1(self,event):
        ent=self.ent_m1.get()#Obtenemos el valor de la caja de texto
        if ent=='':#Si la caja de texto esta vacia
            ent=0#Asignamos 0
        try:
            ent=int(ent)#Convertimos a entero
            tc=ent
            self.total_carga_m1.config(text=(ent*int(self.txtmoneda1)))#Mostramos el total de la carga
            cant_m1=ent+int(self.cantmoneda1)#Total de monedas
            self.cant_tot_m1.config(text=str(cant_m1))#Mostramos la cantidad total
            self.cant_fin_mon1=int(((ent+int(self.cantmoneda1))*int(self.txtmoneda1)))#Se calcula el total final
            self.tot_fin_m1.config(text=self.cant_fin_mon1)#Mostramos el total final
            #Se obtienen las entradas de los otros entrys
            ent2=self.ent_m2.get()
            ent3=self.ent_m3.get()
            if ent2=='':#Si la caja de texto esta vacia
                ent2=0#Asignamos 0
            if ent3=='':
                ent3=0
            #Se calcula el valor de los labels de carga
            self.tot_cant_car_m.config(text=str(int(ent)+int(ent2)+int(ent3)))#Se obtiene el valor de la caja de texto
            self.subres[0]=int(cant_m1)#Se asigna el valor a la lista
            self.tot_carg_tot_m.config(text=str(int(self.total_carga_m1.cget('text'))+int(self.total_carga_m2.cget('text'))+int(self.total_carga_m3.cget('text'))))#Se obtiene el valor del total a cargar
            #Se calculan los datos de los otros labels
            self.sald_cant_tot_m.config(text=str(int(self.cant_tot_m1.cget('text'))+int(self.cant_tot_m2.cget('text'))+int(self.cant_tot_m3.cget('text'))))
            self.sald_tot_m.config(text=str(int(self.tot_fin_m1.cget('text'))+int(self.tot_fin_m2.cget('text'))+int(self.tot_fin_m3.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))#Se calcula el total final del cajero
        except:
            self.ent_m1.delete(0,END)#si no es un número se borra el contenido de la caja de texto
        
    #se hace lo mismo que la anterior pero para el resto de monedas y billetes
        
    def cargar_m2(self,event):
        ent=self.ent_m2.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_m2.config(text=(ent*int(self.txtmoneda2)))
            cant_m2=ent+int(self.cantmoneda2)
            self.cant_tot_m2.config(text=str(cant_m2))
            self.cant_fin_mon2=int(((ent+int(self.cantmoneda2))*int(self.txtmoneda2)))
            self.tot_fin_m2.config(text=self.cant_fin_mon2)
            ent1=self.ent_m1.get()
            ent3=self.ent_m3.get()
            if ent1=='':
                ent1=0
            if ent3=='':
                ent3=0
            self.tot_cant_car_m.config(text=str(int(ent1)+int(ent)+int(ent3)))
            self.subres[1]=int(cant_m2)
            self.tot_carg_tot_m.config(text=str(int(self.total_carga_m1.cget('text'))+int(self.total_carga_m2.cget('text'))+int(self.total_carga_m3.cget('text'))))
            self.sald_cant_tot_m.config(text=str(int(self.cant_tot_m1.cget('text'))+int(self.cant_tot_m2.cget('text'))+int(self.cant_tot_m3.cget('text'))))
            self.sald_tot_m.config(text=str(int(self.tot_fin_m1.cget('text'))+int(self.tot_fin_m2.cget('text'))+int(self.tot_fin_m3.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_m2.delete(0,END)

    def cargar_m3(self,event):
        ent=self.ent_m3.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_m3.config(text=(ent*int(self.txtmoneda3)))
            cant_m3=ent+int(self.cantmoneda3)
            self.cant_tot_m3.config(text=str(cant_m3))
            self.cant_fin_mon3=int(((ent+int(self.cantmoneda3))*int(self.txtmoneda3)))
            self.tot_fin_m3.config(text=self.cant_fin_mon3)
            ent1=self.ent_m1.get()
            ent2=self.ent_m2.get()
            if ent1=='':
                ent1=0
            if ent2=='':
                ent2=0
            self.tot_cant_car_m.config(text=str(int(ent1)+int(ent2)+int(ent)))
            self.subres[2]=int(cant_m3)
            self.tot_carg_tot_m.config(text=str(int(self.total_carga_m1.cget('text'))+int(self.total_carga_m2.cget('text'))+int(self.total_carga_m3.cget('text'))))
            self.sald_cant_tot_m.config(text=str(int(self.cant_tot_m1.cget('text'))+int(self.cant_tot_m2.cget('text'))+int(self.cant_tot_m3.cget('text'))))
            self.sald_tot_m.config(text=str(int(self.tot_fin_m1.cget('text'))+int(self.tot_fin_m2.cget('text'))+int(self.tot_fin_m3.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_m3.delete(0,END)

    ##############################
    #Funciones de cargar billetes
    ##############################

    def cargar_b1(self,event):
        ent=self.ent_b1.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_b1.config(text=(ent*int(self.txtbillet1)))
            cant_b1=ent+int(self.cantbillet1)
            self.cant_tot_b1.config(text=str(cant_b1))
            self.cant_fin_billet1=int(((ent+int(self.cantbillet1))*int(self.txtbillet1)))
            self.tot_fin_b1.config(text=self.cant_fin_billet1)
            ent2=self.ent_b2.get()
            ent3=self.ent_b3.get()
            ent4=self.ent_b4.get()
            ent5=self.ent_b5.get()
            if ent2=='':
                ent2=0
            if ent3=='':
                ent3=0
            if ent4=='':
                ent4=0
            if ent5=='':
                ent5=0
            self.tot_cant_car_b.config(text=str(int(ent2)+int(ent)+int(ent3)+int(ent4)+int(ent5)))
            self.subres[3]=int(cant_b1)
            self.tot_carg_tot_b.config(text=str(int(self.total_carga_b1.cget('text'))+int(self.total_carga_b2.cget('text'))+int(self.total_carga_b3.cget('text'))+int(self.total_carga_b4.cget('text'))+int(self.total_carga_b5.cget('text'))))
            self.sald_cant_tot_b.config(text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))))
            self.sald_tot_b.config(text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_b1.delete(0,END)

    def cargar_b2(self,event):
        ent=self.ent_b2.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_b2.config(text=(ent*int(self.txtbillet2)))
            cant_b2=ent+int(self.cantbillet2)
            self.cant_tot_b2.config(text=str(cant_b2))
            self.cant_fin_billet2=int(((ent+int(self.cantbillet2))*int(self.txtbillet2)))
            self.tot_fin_b2.config(text=self.cant_fin_billet2)
            ent1=self.ent_b1.get()
            ent3=self.ent_b3.get()
            ent4=self.ent_b4.get()
            ent5=self.ent_b5.get()
            if ent1=='':
                ent1=0
            if ent3=='':
                ent3=0
            if ent4=='':
                ent4=0
            if ent5=='':
                ent5=0
            self.tot_cant_car_b.config(text=str(int(ent1)+int(ent)+int(ent3)+int(ent4)+int(ent5)))
            self.subres[4]=int(cant_b2)
            self.tot_carg_tot_b.config(text=str(int(self.total_carga_b1.cget('text'))+int(self.total_carga_b2.cget('text'))+int(self.total_carga_b3.cget('text'))+int(self.total_carga_b4.cget('text'))+int(self.total_carga_b5.cget('text'))))
            self.sald_cant_tot_b.config(text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))))
            self.sald_tot_b.config(text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_b2.delete(0,END)

    def cargar_b3(self,event):
        ent=self.ent_b3.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_b3.config(text=(ent*int(self.txtbillet3)))
            cant_b3=ent+int(self.cantbillet3)
            self.cant_tot_b3.config(text=str(cant_b3))
            self.cant_fin_billet3=int(((ent+int(self.cantbillet3))*int(self.txtbillet3)))
            self.tot_fin_b3.config(text=self.cant_fin_billet3)
            ent1=self.ent_b1.get()
            ent2=self.ent_b2.get()
            ent4=self.ent_b4.get()
            ent5=self.ent_b5.get()
            if ent1=='':
                ent1=0
            if ent2=='':
                ent2=0
            if ent4=='':
                ent4=0
            if ent5=='':
                ent5=0
            self.tot_cant_car_b.config(text=str(int(ent1)+int(ent)+int(ent2)+int(ent4)+int(ent5)))
            self.subres[5]=int(cant_b3)
            self.tot_carg_tot_b.config(text=str(int(self.total_carga_b1.cget('text'))+int(self.total_carga_b2.cget('text'))+int(self.total_carga_b3.cget('text'))+int(self.total_carga_b4.cget('text'))+int(self.total_carga_b5.cget('text'))))
            self.sald_cant_tot_b.config(text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))))
            self.sald_tot_b.config(text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_b3.delete(0,END)

    def cargar_b4(self,event):
        ent=self.ent_b4.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_b4.config(text=(ent*int(self.txtbillet4)))
            cant_b4=ent+int(self.cantbillet4)
            self.cant_tot_b4.config(text=str(cant_b4))
            self.cant_fin_billet4=int(((ent+int(self.cantbillet4))*int(self.txtbillet4)))
            self.tot_fin_b4.config(text=self.cant_fin_billet4)
            ent1=self.ent_b1.get()
            ent2=self.ent_b2.get()
            ent3=self.ent_b3.get()
            ent5=self.ent_b5.get()
            if ent1=='':
                ent1=0
            if ent2=='':
                ent2=0
            if ent3=='':
                ent3=0
            if ent5=='':
                ent5=0
            self.tot_cant_car_b.config(text=str(int(ent1)+int(ent)+int(ent2)+int(ent3)+int(ent5)))
            self.subres[6]=int(cant_b4)
            self.tot_carg_tot_b.config(text=str(int(self.total_carga_b1.cget('text'))+int(self.total_carga_b2.cget('text'))+int(self.total_carga_b3.cget('text'))+int(self.total_carga_b4.cget('text'))+int(self.total_carga_b5.cget('text'))))
            self.sald_cant_tot_b.config(text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))))
            self.sald_tot_b.config(text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_b4.delete(0,END)

    def cargar_b5(self,event):
        ent=self.ent_b5.get()
        if ent=='':
            ent=0
        try:
            ent=int(ent)
            self.total_carga_b5.config(text=(ent*int(self.txtbillet5)))
            cant_b5=ent+int(self.cantbillet5)
            self.cant_tot_b5.config(text=str(cant_b5))
            self.cant_fin_billet5=int(((ent+int(self.cantbillet5))*int(self.txtbillet5)))
            self.tot_fin_b5.config(text=self.cant_fin_billet5)
            ent1=self.ent_b1.get()
            ent2=self.ent_b2.get()
            ent3=self.ent_b3.get()
            ent4=self.ent_b4.get()
            if ent1=='':
                ent1=0
            if ent2=='':
                ent2=0
            if ent3=='':
                ent3=0
            if ent4=='':
                ent4=0
            self.tot_cant_car_b.config(text=str(int(ent1)+int(ent)+int(ent2)+int(ent3)+int(ent4)))
            self.subres[7]=int(cant_b5)
            self.tot_carg_tot_b.config(text=str(int(self.total_carga_b1.cget('text'))+int(self.total_carga_b2.cget('text'))+int(self.total_carga_b3.cget('text'))+int(self.total_carga_b4.cget('text'))+int(self.total_carga_b5.cget('text'))))
            self.sald_cant_tot_b.config(text=str(int(self.cant_tot_b1.cget('text'))+int(self.cant_tot_b2.cget('text'))+int(self.cant_tot_b3.cget('text'))+int(self.cant_tot_b4.cget('text'))+int(self.cant_tot_b5.cget('text'))))
            self.sald_tot_b.config(text=str(int(self.tot_fin_b1.cget('text'))+int(self.tot_fin_b2.cget('text'))+int(self.tot_fin_b3.cget('text'))+int(self.tot_fin_b4.cget('text'))+int(self.tot_fin_b5.cget('text'))))
            self.total_final.config(text=str(int(self.sald_tot_b.cget('text'))+int(self.sald_tot_m.cget('text'))))
        except:
            self.ent_b5.delete(0,END)

    #########################
    #Funciones de botones
    #########################

    def btn_guardar(self):
        ask=messagebox.askquestion("Guardar","¿Desea guardar los cambios?")
        if ask=='yes':
            fk=open('cajero.dat','w')
            fk.write(str(self.subres))
            fk.close()
            messagebox.showinfo("Guardar","Se han guardado los cambios")
            self.destroy()
            cargar_cajero().mainloop()
        else:
            messagebox.showinfo("Guardar","No se han guardado los cambios")

    def btn_cancelar(self):
        ask=messagebox.askquestion("Cancelar","¿Desea cancelar?\nSe perderán los cambios")
        if ask=='yes':
            self.destroy()
            menu_principal().mainloop()
        else:
            messagebox.showinfo("Cancelar","No se ha cancelado")
    
    def btn_vaciar(self):
        ask=messagebox.askquestion("Vaciar","¿Desea vaciar el cajero?")
        if ask=='yes':
            self.subres=[0,0,0,0,0,0,0,0]
            fk=open('cajero.dat','w')
            fk.write(str(self.subres))
            fk.close()
            messagebox.showinfo("Vaciar","Se ha vaciado el cajero")
            self.destroy()
            cargar_cajero().mainloop()
        else:
            messagebox.showinfo("Vaciar","No se ha vaciado el cajero")
class entrada_de_vehiculo(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title('Parqueo-Entrada de vehículos')
        self.geometry('525x350')
        self.resizable(0,0)
        self.iconbitmap('icon.ico')

        fk=open('configuracion.dat','r')
        self.config=fk.read()
        fk.close()
        self.config=eval(self.config)

        pq=open('parqueo.dat','r')
        self.parqueo=pq.read()
        pq.close()
        self.parqueo=eval(self.parqueo)

        fo=('Arial',12)

        col1=20
        col2=250
        fila1=50
        fila2=90
        fila3=130
        fila4=170
        fila5=210
        fila6=250
        self.l1=tkinter.Label(self,text='Entrada de Vehículo',font=('Arial',20))
        self.l1.place(x=125,y=10)

        self.l2=tkinter.Label(self,text='Espacios Disponibles',font=fo)
        self.l2.place(x=col1,y=fila1)

        self.total_espacios=int(int(self.config[0])-int(len(self.parqueo)))

        if self.total_espacios>0:
            self.l3=tkinter.Label(self,text=str(self.total_espacios),font=fo)
        else:
            self.l3=tkinter.Label(self,text='NO HAY ESPACIOS',font=('Arial',20,'bold'),fg='red')

        self.l3.place(x=col2,y=fila1)

        self.l4=tkinter.Label(self,text='Su Placa',font=fo)
        self.l4.place(x=col1,y=fila2)

        self.ent_placa=tkinter.Entry(self,width=10,font=fo,relief='solid')
        self.ent_placa.place(x=col2,y=fila2)

        self.l5=tkinter.Label(self,text='Campo Asignado',font=fo)
        self.l5.place(x=col1,y=fila3)

        if self.total_espacios!=0:
            for i in range(self.config[0]+1):
                if i not in self.parqueo:
                    if i==0:
                        pass
                    else:
                        self.espacio_asignado=i
                        break
        else:
            self.espacio_asignado=0
        
        self.l6=tkinter.Label(self,text=str(self.espacio_asignado),font=fo)
        self.l6.place(x=col2,y=fila3)

        self.l7=tkinter.Label(self,text='Hora de entrada',font=fo)
        self.l7.place(x=col1,y=fila4)

        self.hora_entrada=datetime.datetime.now().strftime('%H:%M %d/%m/%Y')
        self.l8=tkinter.Label(self,text=self.hora_entrada,font=fo)
        self.l8.place(x=col2,y=fila4)

        self.l9=tkinter.Label(self,text='Precio por hora',font=fo)
        self.l9.place(x=col1,y=fila5)

        self.precio_hora=tkinter.Label(self,text=str(self.config[1]),font=fo)
        self.precio_hora.place(x=col2,y=fila5)

        #########################
        #Botones
        #########################

        altura=2
        ancho=10
        fx=('Arial',12)

        self.b1=tkinter.Button(self,text='Ok',bg='blue2',fg='white',font=fx,height=altura,width=ancho,command=self.btn_ok)
        self.b1.place(x=col1+80,y=fila6)

        self.b2=tkinter.Button(self,text='Cancelar',bg='blue2',fg='white',font=fx,height=altura,width=ancho,command=self.btn_cancelar)
        self.b2.place(x=col2,y=fila6)


    def btn_ok(self):
        placa=self.ent_placa.get()
        if self.total_espacios==0:
            messagebox.showinfo("Error","No hay espacios disponibles")
            return
        if placa=='':
            messagebox.showinfo('Error','No ha ingresado la placa')
        else:
            ex=False
            for i in self.parqueo.values():
                if placa in i:
                    ex=True
                    break
            if ex==True:
                messagebox.showinfo('Error','El vehículo ya está en el parqueo')
            else:
                ask=messagebox.askquestion('Guardar','¿Desea registrar el vehículo?')
                if ask=='yes':
                    self.parqueo[self.espacio_asignado]=[placa,self.hora_entrada,0,0,0,self.espacio_asignado]
                    fk=open('parqueo.dat','w')
                    fk.write(str(self.parqueo))
                    fk.close()
                    messagebox.showinfo('Exito','El vehículo ha sido registrado')
                    self.destroy()
                    entrada_de_vehiculo().mainloop
                else:
                    messagebox.showinfo('Cancelado','No se ha registrado el vehículo')
        
    def btn_cancelar(self):
        if self.ent_placa.get()=='':
            self.destroy()
            menu_principal().mainloop()
        else:
            ask=messagebox.askquestion("Cancelar","¿Desea cancelar?\nSe perderán los cambios")
            if ask=='yes':
                self.destroy()
                menu_principal().mainloop()
            else:
                messagebox.showinfo("Cancelar","No se ha cancelado")
class cajero_del_parqueo(tkinter.Tk):
    def __init__(self):
        #Se inicializa la ventana
        tkinter.Tk.__init__(self)
        self.title('Parqueo-Cajero del Parqueo')
        self.geometry('615x650')
        self.resizable(False,False)
        self.iconbitmap('dolar.ico')
        #Se cargan los datos de la configuración
        fk=open('configuracion.dat','r')
        self.config=fk.read()
        fk.close()
        self.config=eval(self.config)
        #Se cargan los datos del parqueo
        fk=open('parqueo.dat','r')
        self.parqueo=fk.read()
        fk.close()
        self.parqueo=eval(self.parqueo)
        #Se cargan los datos del cajero
        fk=open('cajero.dat','r')
        self.cajero=fk.read()
        fk.close()
        self.cajero=eval(self.cajero)

        #Se crean laas variables de posicionamiento
        fo=('Arial',12)
        col1=10
        col2=200
        col3=270
        col4=350
        col5=500
        fila1=10
        fila2=70
        fila3=100
        fila4=130
        fila5=160
        fila6=210
        fila7=240
        fila8=270
        fila9=300
        fila10=330
        fila11=360
        fila12=410
        fila13=440
        fila14=470
        fila15=500
        fila16=530
        fila17=560
        fila18=590

        self.pago=[0,0,0,0,0,0,0,0]
        self.b_m_cambio=[0,0,0,0,0,0,0,0]

        ############################
        #Labels y entradas de paso 1
        #############################

        self.l1=tkinter.Label(self,text='Cajero del Parqueo',font=('Arial',20,'bold'))
        self.l1.place(x=150,y=fila1)

        txtpph=str(self.config[1])+' por hora'
        
        self.l2=tkinter.Label(self,text=txtpph,font=fo)
        self.l2.place(x=col5,y=fila1+10)

        self.l3=tkinter.Label(self,text='Paso 1: Su placa',font=fo)
        self.l3.place(x=col1,y=fila2)

        self.ent_placa=tkinter.Entry(self,width=10,font=fo,relief='solid')
        self.ent_placa.place(x=col2,y=fila2)
        self.ent_placa.bind('<KeyRelease>',self.validar_placa)

        self.l4=tkinter.Label(self,text='Hora de entrada',font=fo)
        self.l4.place(x=col1,y=fila3)

        self.lab_hora_entrada=Label(self,text=0,font=fo)
        self.lab_hora_entrada.place(x=col2,y=fila3)

        self.l5=tkinter.Label(self,text='Hora de salida',font=fo)
        self.l5.place(x=col1,y=fila4)

        self.hora_salida=datetime.datetime.now().strftime('%H:%M %d/%m/%Y')

        self.lab_hora_salida=Label(self,text=self.hora_salida,font=fo)
        self.lab_hora_salida.place(x=col2,y=fila4)

        self.l6=tkinter.Label(self,text='Tiempo cobrado',font=fo)
        self.l6.place(x=col1,y=fila5)

        self.lab_tiempo_cobrado=Label(self,text=0,font=fo)
        self.lab_tiempo_cobrado.place(x=col2,y=fila5)

        self.l7=tkinter.Label(self,text='Total a pagar',font=fo)
        self.l7.place(x=col5,y=fila2)

        self.lab_total_pagar=Label(self,text=0,font=fo,bg='RoyalBlue2',fg='white',height=3,width=10)
        self.lab_total_pagar.place(x=col5,y=fila3)

        ####################
        #Labels del paso 2
        ####################

        self.l8=tkinter.Label(self,text='Paso 2: Su pago en',font=fo)
        self.l8.place(x=col1,y=fila6)

        self.l9=tkinter.Label(self,text='Monedas',font=fo)
        self.l9.place(x=col2-30,y=fila6)

        self.l10=tkinter.Label(self,text='Billetes',font=fo)
        self.l10.place(x=col3,y=fila6)

        self.l11=tkinter.Label(self,text='Tarjeta de crédito',font=fo)
        self.l11.place(x=col4,y=fila6)

        self.tarjeta=tkinter.Entry(self,width=11,font=fo,relief='solid')
        self.tarjeta.place(x=col4,y=fila7)

        self.l12=tkinter.Label(self,text='Pagado',font=fo)
        self.l12.place(x=col5,y=fila6)

        self.lab_pagado=Label(self,text=0,font=fo,bg='RoyalBlue2',fg='white',height=2,width=10)
        self.lab_pagado.place(x=col5,y=fila7)

        self.l13=tkinter.Label(self,text='Cambio',font=fo)
        self.l13.place(x=col5,y=fila8+20)

        ###############################
        #Botones de monedas y billetes
        ###############################

        self.lab_cambio=Label(self,text=0,font=fo,bg='RoyalBlue2',fg='white',height=2,width=10)
        self.lab_cambio.place(x=col5,y=fila9+20)

        self.btn_moneda1=tkinter.Button(self,text=self.config[5],font=fo,command=self.btn_moneda1)
        self.btn_moneda1.place(x=col2-30,y=fila7)

        self.btn_moneda2=tkinter.Button(self,text=self.config[6],font=fo,command=self.btn_moneda2)
        self.btn_moneda2.place(x=col2-30,y=fila9)

        self.btn_moneda3=tkinter.Button(self,text=self.config[7],font=fo,command=self.btn_moneda3)
        self.btn_moneda3.place(x=col2-30,y=fila11)

        self.btn_billetes1=tkinter.Button(self,text=self.config[8],font=fo,command=self.btn_billete1)
        self.btn_billetes1.place(x=col3,y=fila7)

        self.btn_billetes2=tkinter.Button(self,text=self.config[9],font=fo,command=self.btn_billete2)
        self.btn_billetes2.place(x=col3,y=fila8)

        self.btn_billetes3=tkinter.Button(self,text=self.config[10],font=fo,command=self.btn_billete3)
        self.btn_billetes3.place(x=col3,y=fila9)

        self.btn_billetes4=tkinter.Button(self,text=self.config[11],font=fo,command=self.btn_billete4)
        self.btn_billetes4.place(x=col3,y=fila10)

        self.btn_billetes5=tkinter.Button(self,text=self.config[12],font=fo,command=self.btn_billete5)
        self.btn_billetes5.place(x=col3,y=fila11)

        ###############################
        #Labels del paso 3
        ###############################

        self.l14=tkinter.Label(self,text='Paso 3: Su cambio en',font=fo)
        self.l14.place(x=col1,y=fila12)

        self.l15=tkinter.Label(self,text='Monedas',font=fo)
        self.l15.place(x=col2-30,y=fila12)

        self.l16=tkinter.Label(self,text='Billetes',font=fo)
        self.l16.place(x=col3,y=fila12)

        self.cam_m1=Label(self,text='0 De '+str(self.config[5]),font=fo)
        self.cam_m1.place(x=col2-30,y=fila13)

        self.cam_m2=Label(self,text='0 De '+str(self.config[6]),font=fo)
        self.cam_m2.place(x=col2-30,y=fila14)

        self.cam_m3=Label(self,text='0 De '+str(self.config[7]),font=fo)
        self.cam_m3.place(x=col2-30,y=fila15)

        self.cam_b1=Label(self,text='0 De '+str(self.config[8]),font=fo)
        self.cam_b1.place(x=col3,y=fila13)

        self.cam_b2=Label(self,text='0 De '+str(self.config[9]),font=fo)
        self.cam_b2.place(x=col3,y=fila14)

        self.cam_b3=Label(self,text='0 De '+str(self.config[10]),font=fo)
        self.cam_b3.place(x=col3,y=fila15)

        self.cam_b4=Label(self,text='0 De '+str(self.config[11]),font=fo)
        self.cam_b4.place(x=col3,y=fila16)

        self.cam_b5=Label(self,text='0 De '+str(self.config[12]),font=fo)
        self.cam_b5.place(x=col3,y=fila17)

        ###############################
        #Boton
        ###############################

        self.btn_anular=tkinter.Button(self,text='Anular el Pago',font=fo,bg='blue2',fg='white',height=2,width=12,command=self.btn_anular)
        self.btn_anular.place(x=col1,y=fila18)

    def validar_placa(self,event):
        placa=self.ent_placa.get()

        for i in self.parqueo.values():
            if placa in i:
                if i[2]!=0:
                    messagebox.showinfo('Error','El auto ya pagó')
                    break
                else:
                    self.auto_select=i
                    self.hora_entrada=i[1]
                    self.lab_hora_entrada.config(text=self.hora_entrada)
                    #se obtiene la diferencia de horas entrada y salida
                    hora_entrada=datetime.datetime.strptime(self.hora_entrada,'%H:%M %d/%m/%Y')
                    hora_salida=datetime.datetime.strptime(self.hora_salida,'%H:%M %d/%m/%Y')
                    diferencia=hora_salida-hora_entrada
                    self.lab_tiempo_cobrado.config(text=str(diferencia))
                    #se obtiene el total a pagar
                    if ((diferencia.seconds//60)//60)!=0:
                        if ((diferencia.seconds//60)%60)!=0:
                            self.total_a_pagar=int(((((diferencia.seconds//60)//60))*self.config[1])+self.config[2])
                        else:
                            self.total_a_pagar=int((((diferencia.seconds//60)//60)*self.config[1]))
                    else:
                        self.total_a_pagar=self.config[2]
                    self.lab_total_pagar.config(text=str(self.total_a_pagar))
                    self.lab_cambio.config(text=str(0-self.total_a_pagar))
                    break     
            else:
                self.lab_hora_entrada.config(text=0)
                self.lab_tiempo_cobrado.config(text=0)
                self.lab_total_pagar.config(text=0)
                self.lab_cambio.config(text=0)

    def btn_moneda1(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[5]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[5]))
            self.pago[0]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_moneda2(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[6]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[6]))
            self.pago[1]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_moneda3(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[7]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[7]))
            self.pago[2]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_billete1(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[8]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[8]))
            self.pago[3]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_billete2(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[9]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[9]))
            self.pago[4]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_billete3(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[10]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[10]))
            self.pago[5]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_billete4(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[11]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[11]))
            self.pago[6]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def btn_billete5(self):
        self.total_pagar=int(self.lab_total_pagar.cget('text'))
        if self.total_pagar>0:
            subtotal=int(self.lab_pagado.cget('text'))+self.config[12]
            self.lab_pagado.config(text=str(subtotal))
            subcambio=int(self.lab_cambio.cget('text'))
            self.lab_cambio.config(text=str(subcambio+self.config[12]))
            self.pago[7]+=1
            if subtotal>=self.total_pagar:
                self.cambio()
                self.destroy()
                mp=menu_principal()
                mp.mainloop()
        else:
            messagebox.showinfo('Error','Ingrese una placa')

    def cambio(self):
        tot_cambio=int(self.lab_cambio.cget('text'))
        if tot_cambio>0:
            if self.config[12]!=0:
                if tot_cambio>=self.config[12]:
                    cambio_b5=tot_cambio//self.config[12]
                    if cambio_b5>self.cajero[7]:
                        cambio_b5=self.cajero[7]
                    tot_cambio-=cambio_b5*self.config[12]
                    self.b_m_cambio[7]+=cambio_b5
            if self.config[11]!=0:
                if tot_cambio>=self.config[11]:
                    cambio_b4=tot_cambio//self.config[11]
                    if cambio_b4>self.cajero[6]:
                        cambio_b4=self.cajero[6]
                    tot_cambio-=cambio_b4*self.config[11]
                    self.b_m_cambio[6]+=cambio_b4
            if self.config[10]!=0:
                if tot_cambio>=self.config[10]:
                    cambio_b3=tot_cambio//self.config[10]
                    if cambio_b3>self.cajero[5]:
                        cambio_b3=self.cajero[5]
                    tot_cambio-=cambio_b3*self.config[10]
                    self.b_m_cambio[5]+=cambio_b3
            if self.config[9]!=0:
                if tot_cambio>=self.config[9]:
                    cambio_b2=tot_cambio//self.config[9]
                    if cambio_b2>self.cajero[4]:
                        cambio_b2=self.cajero[4]
                    tot_cambio-=cambio_b2*self.config[9]
                    self.b_m_cambio[4]+=cambio_b2
            if self.config[8]!=0:
                if tot_cambio>=self.config[8]:
                    cambio_b1=tot_cambio//self.config[8]
                    if cambio_b1>self.cajero[3]:
                        cambio_b1=self.cajero[3]
                    tot_cambio-=cambio_b1*self.config[8]
                    self.b_m_cambio[3]+=cambio_b1
            
            if self.config[7]!=0:
                if tot_cambio>=self.config[7]:
                    cambio_m3=tot_cambio//self.config[7]
                    if cambio_m3>self.cajero[2]:
                        cambio_m3=self.cajero[2]
                    tot_cambio-=cambio_m3*self.config[7]
                    self.b_m_cambio[2]+=cambio_m3
            if self.config[6]!=0:
                if tot_cambio>=self.config[6]:
                    cambio_m2=tot_cambio//self.config[6]
                    if cambio_m2>self.cajero[1]:
                        cambio_m2=self.cajero[1]
                    tot_cambio-=cambio_m2*self.config[6]
                    self.b_m_cambio[1]+=cambio_m2
            if self.config[5]!=0:
                if tot_cambio>=self.config[5]:
                    cambio_m1=tot_cambio//self.config[5]
                    if cambio_m1>self.cajero[0]:
                        cambio_m1=self.cajero[0]
                    tot_cambio-=cambio_m1*self.config[5]
                    self.b_m_cambio[0]+=cambio_m1

            if tot_cambio!=0:
                messagebox.showinfo('Error','No hay suficiente cambio')
            else:
                self.cam_b5.config(text=str(self.b_m_cambio[7])+' De '+str(self.config[12]))
                self.cam_b4.config(text=str(self.b_m_cambio[6])+' De '+str(self.config[11]))
                self.cam_b3.config(text=str(self.b_m_cambio[5])+' De '+str(self.config[10]))
                self.cam_b2.config(text=str(self.b_m_cambio[4])+' De '+str(self.config[9]))
                self.cam_b1.config(text=str(self.b_m_cambio[3])+' De '+str(self.config[8]))
                self.cam_m3.config(text=str(self.b_m_cambio[2])+' De '+str(self.config[7]))
                self.cam_m2.config(text=str(self.b_m_cambio[1])+' De '+str(self.config[6]))
                self.cam_m1.config(text=str(self.b_m_cambio[0])+' De '+str(self.config[5]))
                messagebox.showinfo('Cambio','Cambio: '+str(self.lab_cambio.cget('text'))+'\nGracias por su visita\nCuenta con '+str(self.config[4])+' minutos para salir')
                for i in range(len(self.cajero)):
                    self.cajero[i]+=self.pago[i]
                    self.cajero[i]-=self.b_m_cambio[i]
                
                fk=open('cajero.dat','w')
                fk.write(str(self.cajero))
                fk.close()
                a_pagar=self.auto_select[3]
                a_pagar+=self.total_a_pagar
                newdato=[self.auto_select[0],self.auto_select[1],self.hora_salida,a_pagar,0,self.auto_select[5]]

                self.parqueo[self.auto_select[5]]=newdato

                fk=open('parqueo.dat','w')
                fk.write(str(self.parqueo))
                fk.close()

    def btn_anular(self):
        ask=messagebox.askquestion('Anular','¿Esta seguro de anular el pago?')
        if ask=='yes':
            messagebox.showinfo('Anulado','Pago anulado')
            self.destroy()
            mp=menu_principal()
            mp.mainloop()
class salida_de_vehiculo(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title('Parqueo-Salida de Vehiculo')
        self.geometry('500x175')
        self.resizable(0,0)
        self.iconbitmap('icon.ico')

        fk=open('configuracion.dat','r')
        self.config=eval(fk.read())
        fk.close()

        fk=open('parqueo.dat','r')
        self.parqueo=eval(fk.read())
        fk.close()

        self.l1=tkinter.Label(self,text='Salida de vehículo',font=('Arial',20,'bold'))
        self.l1.place(x=125,y=10)

        self.l2=tkinter.Label(self,text='Placa:',font=('Arial',14))
        self.l2.place(x=50,y=60)

        self.ent_placa=tkinter.Entry(self,width=10,font=('Arial',14),relief='solid')
        self.ent_placa.place(x=140,y=60)

        self.btn_salida=tkinter.Button(self,text='Ok',command=self.btn_salida,bg='blue2',fg='white',width=7,font=('Arial',14))
        self.btn_salida.place(x=50,y=110)

        self.btn_cancelar=tkinter.Button(self,text='Cancelar',command=self.btn_cancelar,bg='blue2',fg='white',width=7,font=('Arial',14))
        self.btn_cancelar.place(x=200,y=110)


    def btn_salida(self):
        placa=self.ent_placa.get()
        if placa=='':
            messagebox.showinfo('Error','Ingrese la placa')
        else:
            for pos_i,i in enumerate(self.parqueo.values()):
                if i[0]==placa:
                    if i[3]==0:
                        messagebox.showinfo('Error','El vehículo no ha pagado')
                        return
                    else:
                        hora_pago=datetime.datetime.strptime(i[2],'%H:%M %d/%m/%Y')
                        hora_salida=datetime.datetime.now().strftime('%H:%M %d/%m/%Y')
                        hora_salida=datetime.datetime.strptime(hora_salida,'%H:%M %d/%m/%Y')
                        dif_tiempo=hora_salida-hora_pago
                        if dif_tiempo.seconds%60 > 0 or dif_tiempo.seconds//60>self.config[4]:
                            messagebox.showinfo('Error','Tiempo de salida excedido\nDebe regresar a pagar la diferencia')
                            self.parqueo[pos_i+1][1]=datetime.datetime.now().strftime('%H:%M %d/%m/%Y')
                            self.parqueo[pos_i+1][2]=0
                            fk=open('parqueo.dat','w')
                            fk.write(str(self.parqueo))
                            fk.close()
                            return
                        else:
                            del self.parqueo[i[5]]
                            print(self.parqueo)
                            fk=open('parqueo.dat','w')
                            fk.write(str(self.parqueo))
                            fk.close()
                        messagebox.showinfo('Salida','Gracias por su visita')
                        return
            messagebox.showinfo('Salida','El vehículo no está registrado')

    def btn_cancelar(self):
        self.destroy()
        mp=menu_principal()
        mp.mainloop()

menu_principal().mainloop()