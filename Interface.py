import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
#import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from tkinter import messagebox, ttk


root = tk.Tk() #crea ventana principal e inicia intérprete Tcñ y TK
root.title("Brazo robótico 4 grados de libertad")
root.config(width=1024, height=768)

#Marcha/Paro/Reset
marco_p = LabelFrame(text="Ejecución programa", padx=0, pady=0).place(height=170, width=150, x=10, y=0)
marcha = Button(root, text="START", height=1, width=5, bg="Light Green").place(x=20, y=40)
et_marcha = Label(text="Inicio").place(x=80, y=40)
paro = Button(root, text="STOP", height=1, width=5, bg="Tomato").place(x=20, y=80)
et_paro = Label(text="Paro").place(x=80, y=80)
reset = Button(root, text="RESET",height=1, width=5, bg="Light Blue").place(x=20, y=120)
et_reset = Label(text="Reestablecer").place(x=80, y=120)

#Ventana Reset
#messasge = MessageBox.showinfo("Reset", "El programa se reestablecerá a los valores predeterminados\n ¿Desea continuar?")

#Marcha/Paro/Reset Frames
Marchaf=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=40)
Parof=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=80)
Resetf=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=120)

#coordenadas cartesianas
marco1 = LabelFrame(text="Coordenadas Herramienta: ", padx=0, pady=0).place(height=200 , width=170 , x=450 , y=0 )
Xpos = Button(root, text='X+')
Xpos.place(x=570, y=40)
Xneg = Button(root, text='X-')
Xneg.place(x=470, y=40)
coord_x=Label(text='Eje X').place(x=515, y=20)
marco_x=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=515, y=40)
Ypos = Button(root, text='Y+')
Ypos.place(x=570, y=90)
Yneg = Button(root, text='Y-')
Yneg.place(x=470, y=90)
coord_y=Label(text='Eje Y').place(x=515, y=70)
marco_y=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=515, y=90)
Zpos = Button(root, text='Z+')
Zpos.place(x=570, y=140)
Zneg = Button(root, text='Z-')
Zneg.place(x=470, y=140)
coord_z=Label(text='Eje Z').place(x=515, y=120)
marco_z=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=515, y=140)

#Articulaciones
marco2 = LabelFrame(text="Movimiento Articulaciones: ", padx=0, pady=0).place(height=360 , width=230 , x=210 , y=0 )

#Información servomotor
var = DoubleVar
angle = Scale(root, variable=var, orient = HORIZONTAL, from_= -90, to = 90, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Servomotor angle')
angle.set(0)
angle.place(x=220, y=20)

#Articulación1
var1 = DoubleVar
cintura = Scale(root, variable=var1, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Cintura(Q1)')
cintura.set(0) #pos home dexarm (AÑADIR)
cintura.place(x=220, y=80)

#Articulación 2
var2 = DoubleVar
hombro = Scale(root, variable=var2, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Hombro(Q2)')
hombro.set(0) #pos home dexarm (AÑADIR)
hombro.place(x=220, y=140)

#Articulación 3
var3 = DoubleVar
codo = Scale(root, variable=var3, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Codo(Q3)')
codo.set(0) #pos home dexarm (AÑADIR)
codo.place(x=220, y=210)

#Articulación 4
var4 = DoubleVar
muñeca = Scale(root, variable=var4, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Muñeca(Q4)')
muñeca.set(0) #pos home dexarm (AÑADIR)
muñeca.place(x=220, y=270)

#selección velocidad
#def selection_changed(event):
    #selection = velocidad.get()
    #messagebox.showinfo(tittle="Nuevo elemento seleccionado", message=selection)

marco_vel = LabelFrame(text="Velocidad: ", padx=0, pady=0).place(height=50 , width=165 , x=10 , y=230 )
velocidad = ttk.Combobox(values=["Lenta", "Rápida"])
velocidad.place(x=20, y=250)
#velocidad.bind("<<ComboboxSelected>>", selection_changed)


#pantalla de inicio
def widgets(self):
    title = Label(self.root, font='Arial', text='SOFTWARE ROTRICS: \nSoftware de Control Remoto del DexArm')
    title.pack(ipady=5)
    frame = Frame(self.root)
    frame.pack()

#Calibración
calibracion = Button(root, text="Calibración", height=1, width=10, bg="salmon1").place(x=20, y=190)
#Comandos

#Movimientos Predeterminados

#Movimiento Lineal

#Movimiento Circular

#Funciones predeterminadas
#Cuadrado

#Círculo

#Posición actual
pos = LabelFrame(text="Posición actual", padx=0, pady=0).place(height=70, width=1000, x=10, y=680)
pos_x=Label(text='Eje X').place(x=20, y=710)
marco_posx=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=55, y=710)
pos_y=Label(text='Eje Y').place(x=100, y=710)
marco_posy=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=135, y=710)
pos_z=Label(text='Eje Z').place(x=180, y=710)
marco_posz=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=215, y=710)
pos_q1=Label(text='Q1').place(x=260, y=710)
marco_posq1=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=295, y=710)
pos_q2=Label(text='Q2').place(x=340, y=710)
marco_posq2=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=375, y=710)
pos_q3=Label(text='Q3').place(x=420, y=710)
marco_posq3=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=455, y=710)
pos_q4=Label(text='Q4').place(x=500, y=710)
marco_posq4=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=535, y=710)
#bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()