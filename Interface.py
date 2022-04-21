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

B_ON = Button(root, text='Inicio')
B_ON.place(bordermode=INSIDE)
B_OFF = Button(root, text='Final')
B_OFF.place()

#pantalla de inicio
def widgets(self):
    title = Label(self.root, font='Arial', text='SOFTWARE ROTRICS: \nSoftware de Control Remoto del DexArm')
    title.pack(ipady=5)
    frame = Frame(self.root)
    frame.pack()

#bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()