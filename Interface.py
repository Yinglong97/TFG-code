import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
# import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from tkinter import messagebox, ttk
from tkinter import messagebox as mb
import time

root = tk.Tk()  # crea ventana principal e inicia intérprete Tcl y TK
root.title("Brazo robótico 4 grados de libertad")
root.config(width=630, height=520)
root.resizable(False, False)

# MARHCA/PARO/RESET
marco_p = LabelFrame(text="Ejecución programa", padx=0, pady=0).place(height=170, width=150, x=10, y=0)
marcha = Button(root, text="START", height=1, width=5, bg="Light Green").place(x=20, y=40)
et_marcha = Label(text="Inicio").place(x=80, y=40)
paro = Button(root, text="STOP", height=1, width=5, bg="Tomato").place(x=20, y=80)
et_paro = Label(text="Paro").place(x=80, y=80)
reset = Button(root, text="RESET", height=1, width=5, bg="Light Blue").place(x=20, y=120)
et_reset = Label(text="Reestablecer").place(x=80, y=120)

# VENTANA RESET
# messasge = MessageBox.showinfo("Reset", "El programa se reestablecerá a los valores predeterminados\n ¿Desea continuar?")

# Marcha/Paro/Reset Frames
Marchaf = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=40)
Parof = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=80)
Resetf = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=120)

# COORDENADAS CARTESIANAS

valor_x = 0
limit = 100
release = TRUE

#def click_xpos():
#    global valor_x
#    while not Xpos.
#            release and int(marcox.get()) < limit:
#        time.sleep(0.1)
#        marcox.set((str(int(marcox.get()))+1))

#def click_xneg():

#def click_ypos():

#def click_yneg():

#def click_zpos():

#def click_yneg():

incremento = 0

def update_spinboxes_increment(inc):
    #Iterate over all spinBoxes to update the increment
    for spinbox in spinboxes.values():
        spinbox.config(increment=inc)


def selection(event=None):
    seleccion = precision_box.current()
    incremento = 0
    if seleccion == 0:
        incremento = 1
    if seleccion == 1:
        incremento = 0.5
    if seleccion == 2:
        incremento = 0.05
    update_spinboxes_increment(incremento)

marco1 = LabelFrame(text="Coordenadas Herramienta: ", padx=0, pady=0).place(height=220, width=170, x=450, y=0)
label_precision = Label(text="Precisión").place(x=470, y=20)
precision_box = ttk.Combobox(values=[".", ".0", ".00"], width=5, postcommand=selection)
precision_box.place(x=540, y=20)
precision_box.bind('<<ComboboxSelected>>', selection)

#Build and locate spinboxes
spinboxes = {}
spinboxes['xpos'] = Spinbox(from_=0, to=500, width=5, increment=incremento)
spinboxes['xpos'].place(x=550, y=70)

spinboxes['xneg'] = Spinbox(from_=-500, to=0, width=5, increment=incremento)
spinboxes['xneg'].place(x=470, y=70)

spinboxes['Ypos'] = Spinbox(from_=0, to=500, width=5, increment=incremento)
spinboxes['Ypos'].place(x=550, y=120)

spinboxes['Yneg'] = Spinbox(from_=-500, to=0, width=5, increment=incremento)
spinboxes['Yneg'].place(x=470, y=120)

spinboxes['Zpos'] = Spinbox(from_=0, to=500, width=5, increment=incremento)
spinboxes['Zpos'].place(x=550, y=170)

spinboxes['Zneg'] = Spinbox(from_=-500, to=0, width=5, increment=incremento)
spinboxes['Zneg'].place(x=470, y=170)

#Build and Locate labels
coord_x = Label(text='Eje X').place(x=515, y=70)
coord_y = Label(text='Eje Y').place(x=515, y=120)
coord_z = Label(text='Eje Z').place(x=515, y=170)

# IR A
ir_a = LabelFrame(text="Ir a: ", padx=0, pady=0).place(height=180, width=170, x=450, y=240)
lab_pos_x = Label(text="Posición X:").place(x=460, y=260)
data_pos_x = tk.StringVar()
entry_pos_x = Entry(root).place(height=25, width=35, x=540, y=260)
#pos_x = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=260)
#entry_pos_x = ttk.Entry(pos_x, textvariable=data_pos_x)
lab_pos_y = Label(text="Posición Y:").place(x=460, y=300)
data_pos_y = tk.StringVar()
entry_pos_y = Entry(root).place(height=25, width=35, x=540, y=300)
#pos_y = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=300)
#entry_pos_y = ttk.Entry(pos_y, textvariable=data_pos_y)
lab_pos_z = Label(text="Posición Z:").place(x=460, y=340)
data_pos_z = tk.StringVar()
entry_pos_z = Entry(root).place(height=25, width=35, x=540, y=340)
#pos_z = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=340)
#entry_pos_z = ttk.Entry(pos_z, textvariable=data_pos_z)
go = Button(root, text="Ir", bg="Yellow Green").place(x=520, y=380)

# ARTICULACIONES
marco2 = LabelFrame(text="Movimiento Articulaciones: ", padx=0, pady=0).place(height=360, width=230, x=210, y=0)

# INFORMACIÓN SERVOMOTOR
var = DoubleVar
angle = Scale(root, variable=var, orient=HORIZONTAL, from_=-90, to=90, length=200, width=20, cursor='dot',
              troughcolor='gray', highlightcolor='white', label='Servomotor angle')
angle.set(0)
angle.place(x=220, y=20)

# ARTICULACIÓN 1
var1 = DoubleVar
cintura = Scale(root, variable=var1, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
                troughcolor='gray', highlightcolor='white', label='Cintura(Q1)')
cintura.set(0)  # pos home dexarm (AÑADIR)
cintura.place(x=220, y=80)

# ARTICULACIÓN 2
var2 = DoubleVar
hombro = Scale(root, variable=var2, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
               troughcolor='gray', highlightcolor='white', label='Hombro(Q2)')
hombro.set(0)  # pos home dexarm (AÑADIR)
hombro.place(x=220, y=140)

# ARTICULACIÓN 3
var3 = DoubleVar
codo = Scale(root, variable=var3, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
             troughcolor='gray', highlightcolor='white', label='Codo(Q3)')
codo.set(0)  # pos home dexarm (AÑADIR)
codo.place(x=220, y=210)

# ARTICULACIÓN 4
var4 = DoubleVar
muñeca = Scale(root, variable=var4, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
               troughcolor='gray', highlightcolor='white', label='Muñeca(Q4)')
muñeca.set(0)  # pos home dexarm (AÑADIR)
muñeca.place(x=220, y=270)

# velocidad.bind("<<ComboboxSelected>>", selection_changed)
# selección velocidad
# def selection_changed(event):
# selection = velocidad.get()
# messagebox.showinfo(tittle="Nuevo elemento seleccionado", message=selection)

marco_vel = LabelFrame(text="Velocidad: ", padx=0, pady=0).place(height=50, width=165, x=242.5, y=370)
velocidad = ttk.Combobox(values=["Lenta", "Rápida"]).place(x=252.5, y=390)

# pantalla de inicio
#def widgets(self):
#    title = Label(self.root, font='Arial', text='SOFTWARE ROTRICS: \nSoftware de Control Remoto del DexArm')
#    title.pack(ipady=5)
#    frame = Frame(self.root)
#    frame.pack()

# TRAYECTORIAS
marco_movs = LabelFrame(text="Trayectorias: ", padx=0, pady=0).place(height=250, width=150, x=10, y=180)

# MOVIMIENTO LINEAL
def openwindow1():
    window1 = Toplevel(root)
    window1.title("Movimiento Lineal")
    window1.geometry("250x120")
    label1 = ttk.Label(window1, text="Posición Inicial").place(x=10, y=10)
    data1 = tk.StringVar()
    entry1 = Entry(window1).place(height=20, width=75, x=150, y=10)
    #marco_entry1 = Frame(window1, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=10)
    #entry1 = ttk.Entry(marco_entry1, textvariable=data1)
    label2 = ttk.Label(window1, text="Posición Final").place(x=10, y=40)
    data2 = tk.StringVar()
    entry2 = Entry(window1).place(height=20, width=75, x=150, y=40)
    #marco_entry2 = Frame(window1, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=40)
    #entry2 = ttk.Label(marco_entry2, textvariable=data2)
    mov = ttk.Button(window1, text="Movimiento").place(x=85, y=80)

movlineal = Button(root, text="Movimiento Lineal", height=1, width=15, bg="khaki", command = openwindow1).place(x=20, y=255)
movlineal_frame = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=255)

#    def menu(self):
#        self.menu1 = tk.Menu(self.window1)
#        self.window1.config(menu=self.menu1)
#        self.options1 = tk.Menu(self.menu1, tearoff=0)
#        self.options1.add_command(label="Info...", command=self.info)
#        self.menu1.add_cascade(label="Options", menu=self.options1)
#
#    def movement():
#        if self.data1.get() == "" or self.data2.get() == "":
#            mb.showerror("Warning", "La casilla está vacía")
#        else:
#            self.window1.tittle("Mov.lineal")
#
#    def info():
#        mb.showinfo("Información", "Realiza un movimiento recto desde el punto inicial hasta el final")
#
#
#linealmove = MovLineal()

# MOVIMIENTO CIRCULAR
def openwindow2():
    window2 = Toplevel(root)
    window2.title("Movimiento Circular")
    window2.geometry("250x120")
    label1 = ttk.Label(window2, text="Posición Inicial").place(x=10, y=10)
    data1 = tk.StringVar()
    entry1 = Entry(window2).place(height=20, width=75, x=150, y=10)
    #marco_entry1 = Frame(window2, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=10)
    #entry1 = ttk.Entry(marco_entry1, textvariable=data1)
    label2 = ttk.Label(window2, text="Posición Final").place(x=10, y=40)
    data2 = tk.StringVar()
    entry2 = Entry(window2).place(height=20, width=75, x=150, y=40)
    #marco_entry2 = Frame(window2, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=40)
    #entry2 = ttk.Label(marco_entry2, textvariable=data2)
    mov = ttk.Button(window2, text="Movimiento").place(x=85, y=80)

movcirc = Button(root, text="Movimiento Circular", height=1, width=15, bg="khaki", command = openwindow2).place(x=20, y=295)
movcirc_frame = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=295)

# CUADRADO
def openwindow3():
    window3 = Toplevel(root)
    window3.title("Movimiento Lineal")
    window3.geometry("250x120")
    label1 = ttk.Label(window3, text="Posición Inicial").place(x=10, y=10)
    data1 = tk.StringVar()
    entry1 = Entry(window3).place(height=20, width=75, x=150, y=10)
    #marco_entry1 = Frame(window3, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=10)
    #entry1 = ttk.Entry(marco_entry1, textvariable=data1)
    label2 = ttk.Label(window3, text="Posición Final").place(x=10, y=40)
    data2 = tk.StringVar()
    entry2 = Entry(window3).place(height=20, width=75, x=150, y=40)
    #marco_entry2 = Frame(window3, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=40)
    #entry2 = ttk.Label(marco_entry2, textvariable=data2)
    mov = ttk.Button(window3, text="Movimiento").place(x=85, y=80)

cuadrado = Button(root, text="Cuadrado", height=1, width=15, bg="khaki", command = openwindow3).place(x=20, y=335)
cuadrado_frame = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=335)

# CÍRCULO
def openwindow4():
    window4 = Toplevel(root)
    window4.title("Círculo")
    window4.geometry("250x120")
    label1 = ttk.Label(window4, text="Posición Inicial").place(x=10, y=10)
    data1 = tk.StringVar()
    entry1 = Entry(window4).place(height=20, width=75, x=150, y=10)
    #marco_entry1 = Frame(window4, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=10)
    #entry1 = ttk.Entry(marco_entry1, textvariable=data1)
    label2 = ttk.Label(window4, text="Posición Final").place(x=10, y=40)
    data2 = tk.StringVar()
    entry2 = Entry(window4).place(height=20, width=75, x=150, y=40)
    #marco_entry2 = Frame(window4, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=40)
    #entry2 = ttk.Label(marco_entry2, textvariable=data2)
    mov = ttk.Button(window4, text="Movimiento").place(x=85, y=80)

circulo = Button(root, text="Círculo", height=1, width=15, bg="khaki", command = openwindow4).place(x=20, y=375)
circulo_frame = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=375)

# CALIBRACIÓN
def openwindow5():
    window5 = Toplevel(root)
    window5.title("Círculo")
    window5.geometry("250x120")
    label1 = ttk.Label(window5, text="Tamaño Aguja").place(x=10, y=10)
    data1 = tk.StringVar()
    entry1 = Entry(window5).place(height=20, width=75, x=150, y=10)
    #marco_entry1 = Frame(window5, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=10)
    #entry1 = ttk.Entry(marco_entry1, textvariable=data1)
    label2 = ttk.Label(window5, text="Distancia Base").place(x=10, y=40)
    data2 = tk.StringVar()
    entry2 = Entry(window5).place(height=20, width=75, x=150, y=40)
    #marco_entry2 = Frame(window5, bd=1, relief="groove", background="white").place(height=20, width=75, x=150, y=40)
    #entry2 = ttk.Label(marco_entry2, textvariable=data2)
    mov = ttk.Button(window5, text="Calibrar").place(x=85, y=80)

calibracion = Button(root, text="Calibración", height=1, width=15, bg="khaki", command=openwindow5).place(x=20, y=215)
calibracion_frame = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=215)

# POSICIÓN ACTUAL
pos = LabelFrame(text="Posición actual", padx=0, pady=0).place(height=70, width=610, x=10, y=440)
pos_x1 = Label(text='Eje X').place(x=35, y=470)
marco_posx = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=70, y=470)
pos_y1 = Label(text='Eje Y').place(x=115, y=470)
marco_posy = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=150, y=470)
pos_z1 = Label(text='Eje Z').place(x=195, y=470)
marco_posz = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=230, y=470)
pos_q1 = Label(text='Q1').place(x=275, y=470)
marco_posq1 = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=310, y=470)
pos_q2 = Label(text='Q2').place(x=355, y=470)
marco_posq2 = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=390, y=470)
pos_q3 = Label(text='Q3').place(x=435, y=470)
marco_posq3 = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=470, y=470)
pos_q4 = Label(text='Q4').place(x=515, y=470)
marco_posq4 = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=550, y=470)

# bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()