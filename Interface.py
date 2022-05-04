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

#Información servomotor
var = DoubleVar
angle = Scale(root, variable=var, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Servomotor angle')
angle.set(0)
angle.place(bordermode=OUTSIDE)

#coordenadas cartesianas
Xpos = Button(root, text='X+')
Xpos.place(x=350, y=20)
Xneg = Button(root, text='X-')
Xneg.place(x=250, y=20)
coord_x=Label(text='Eje X').place(x=300, y=0)
marco_x=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=295, y=20)
Ypos = Button(root, text='Y+')
Ypos.place(x=350, y=70)
Yneg = Button(root, text='Y-')
Yneg.place(x=250, y=70)
coord_y=Label(text='Eje Y').place(x=300, y=50)
marco_y=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=295, y=70)
Zpos = Button(root, text='Z+')
Zpos.place(x=350, y=120)
Zneg = Button(root, text='Z-')
Zneg.place(x=250, y=120)
coord_z=Label(text='Eje Z').place(x=300, y=100)
marco_z=Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=295, y=120)

#Articulaciones
#Articulación1
var1 = DoubleVar
cintura = Scale(root, variable=var1, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Cintura(Q1)')
cintura.set(0) #pos home dexarm (AÑADIR)
cintura.place(x=0, y=70)

#Articulación 2
var2 = DoubleVar
hombro = Scale(root, variable=var2, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Hombro(Q1)')
hombro.set(0) #pos home dexarm (AÑADIR)
hombro.place(x=0, y=130)

#Articulación 3
var3 = DoubleVar
codo = Scale(root, variable=var3, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Codo(Q1)')
codo.set(0) #pos home dexarm (AÑADIR)
codo.place(x=0, y=200)

#Articulación 4
var4 = DoubleVar
muñeca = Scale(root, variable=var4, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Muñeca(Q1)')
muñeca.set(0) #pos home dexarm (AÑADIR)
muñeca.place(x=0, y=260)


#pantalla de inicio
def widgets(self):
    title = Label(self.root, font='Arial', text='SOFTWARE ROTRICS: \nSoftware de Control Remoto del DexArm')
    title.pack(ipady=5)
    frame = Frame(self.root)
    frame.pack()

#bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()