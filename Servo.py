import time
import pyfirmata
from pyfirmata import Arduino, util, SERVO
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

#config puerto Arduino y pin Servo
board = Arduino('COM3')
time.sleep(5)
board.digital[7].mode = SERVO
#movimiento Servo

def Servo(pos):
    board.digital[7].write(pos)

#interfaz de prueba
root = tk.Tk() #crea ventana principal e inicia intérprete Tcñ y TK
root.title("Servomotor")
root.config(width=350, height=150)

#Información servomotor
var = DoubleVar
angle = Scale(root, variable=var, orient = HORIZONTAL, from_= 0, to = 180, length = 200, width = 20, cursor = 'dot', troughcolor = 'gray', highlightcolor = 'white', label = 'Servomotor angle', command=Servo)
angle.set(90)
angle.place(x=120, y=20)

root.mainloop()