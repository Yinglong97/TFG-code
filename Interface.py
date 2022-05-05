import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


root = tk.Tk() #crea ventana principal e inicia intérprete Tcñ y TK
root.title("Brazo robótico 4 grados de libertad")
root.config(width=640, height=480)
#cerrar = tkinter.Button(root, text='Salir', command=root.iconify)
##Ventana principal
#def ventana():
#    v1 = tkinter.toplevel(root)
#    root.iconify()
#root = tkinter.Tk()
#pantalla1 = tkinter.Button(root, text="Movimiento", command=ventana)
#pantalla1.pack()

#Marcha/Paro/Reset

#coordenadas cartesianas
marco1 = LabelFrame(text="Coordenadas Herramienta: ", padx=0, pady=0).place(height=200 , width=170 , x=250 , y=0 )
Xpos = Button(root, text='X+')
Xpos.place(x=370, y=40)
Xneg = Button(root, text='X-')
Xneg.place(x=270, y=40)
coord_x=Label(text='Eje X').place(x=315, y=20)
marco_x=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=315, y=40)
Ypos = Button(root, text='Y+')
Ypos.place(x=370, y=90)
Yneg = Button(root, text='Y-')
Yneg.place(x=270, y=90)
coord_y=Label(text='Eje Y').place(x=315, y=70)
marco_y=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=315, y=90)
Zpos = Button(root, text='Z+')
Zpos.place(x=370, y=140)
Zneg = Button(root, text='Z-')
Zneg.place(x=270, y=140)
coord_z=Label(text='Eje Z').place(x=315, y=120)
marco_z=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=315, y=140)

#Articulaciones
marco2 = LabelFrame(text="Movimiento Articulaciones: ", padx=0, pady=0).place(height=360 , width=230 , x=10 , y=0 )

#Información servomotor
var = DoubleVar
angle = Scale(root, variable=var, orient = HORIZONTAL, from_= -90, to = 90, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Servomotor angle')
angle.set(0)
angle.place(x=20, y=20)

#Articulación1
var1 = DoubleVar
cintura = Scale(root, variable=var1, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Cintura(Q1)')
cintura.set(0) #pos home dexarm (AÑADIR)
cintura.place(x=20, y=80)

#Articulación 2
var2 = DoubleVar
hombro = Scale(root, variable=var2, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Hombro(Q2)')
hombro.set(0) #pos home dexarm (AÑADIR)
hombro.place(x=20, y=140)

#Articulación 3
var3 = DoubleVar
codo = Scale(root, variable=var3, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Codo(Q3)')
codo.set(0) #pos home dexarm (AÑADIR)
codo.place(x=20, y=210)

#Articulación 4
var4 = DoubleVar
muñeca = Scale(root, variable=var4, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Muñeca(Q4)')
muñeca.set(0) #pos home dexarm (AÑADIR)
muñeca.place(x=20, y=270)


#pantalla de inicio
def widgets(self):
    title = Label(self.root, font='Arial', text='SOFTWARE ROTRICS: \nSoftware de Control Remoto del DexArm')
    title.pack(ipady=5)
    frame = Frame(self.root)
    frame.pack()

#Calibración

#Comandos

#Movimientos Predeterminados
#Movimiento Lineal

#Movimiento Circular

#Funciones predeterminadas
#Cuadrado

#Círculo


#bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()