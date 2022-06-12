import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
# import serial
from tkinter import messagebox, ttk
from tkinter import messagebox as mb
import time

root = tk.Tk()  # crea ventana principal e inicia intérprete Tcl y TK
root.title("Brazo robótico 4 grados de libertad + 1 (5GDL)")
root.config(width=630, height=540)
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand="yes")
frame1 = ttk.Frame(notebook, height=520, width=630)
frame2 = ttk.Frame(notebook, height=520, width=630)
notebook.add(frame1, text="Control de Movimiento")
notebook.add(frame2, text="Trayectorias")

# MARHCA/PARO/RESET
marco_p = LabelFrame(frame1, text="Ejecución programa", padx=0, pady=0).place(height=210, width=150, x=10, y=10)
marcha = Button(frame1, text="START", height=1, width=5, bg="Light Green").place(x=20, y=50)
et_marcha = Label(frame1, text="Inicio").place(x=80, y=50)
paro = Button(frame1, text="STOP", height=1, width=5, bg="Tomato").place(x=20, y=90)
et_paro = Label(frame1, text="Paro").place(x=80, y=90)
reset = Button(frame1, text="RESET", height=1, width=5, bg="Light Blue").place(x=20, y=130)
et_reset = Label(frame1, text="Reestablecer").place(x=80, y=130)
home = Button(frame1, text="HOME", height=1, width=5, bg="khaki").place(x=20, y=170)
et_home = Label(frame1, text="Punto Inicio").place(x=80, y=170)

# VENTANA RESET
# messasge = MessageBox.showinfo("Reset", "El programa se reestablecerá a los valores predeterminados\n ¿Desea continuar?")

# Marcha/Paro/Reset Frames
Marchaf = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=50)
Parof = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=90)
Resetf = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=130)
Homef = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=170)

# COORDENADAS CARTESIANAS

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
        incremento = 0.1
    update_spinboxes_increment(incremento)

marco1 = LabelFrame(frame1, text="Coordenadas Herramienta: ", padx=0, pady=0).place(height=200, width=185, x=10, y=230)
label_precision = Label(frame1, text="Precisión").place(x=40, y=255)
precision_box = ttk.Combobox(frame1, values=[".", ".0"], width=5, postcommand=selection)
precision_box.place(x=100, y=255)
precision_box.bind('<<ComboboxSelected>>', selection)

#Build and locate spinboxes
spinboxes = {}
spinboxes['xpos'] = Spinbox(frame1, from_=0, to=500, width=7, increment=incremento)
spinboxes['xpos'].place(x=100, y=295)

spinboxes['Ypos'] = Spinbox(frame1, from_=0, to=500, width=7, increment=incremento)
spinboxes['Ypos'].place(x=100, y=345)

spinboxes['Zpos'] = Spinbox(frame1, from_=0, to=500, width=7, increment=incremento)
spinboxes['Zpos'].place(x=100, y=395)

#Build and Locate labels
coord_x = Label(frame1, text='Eje X').place(x=40, y=295)
coord_y = Label(frame1, text='Eje Y').place(x=40, y=345)
coord_z = Label(frame1, text='Eje Z').place(x=40, y=395)

# IR A
#IR A COORDENADAS ARTICULARES
ir_a1 = LabelFrame(frame1, text="Ir a coordenadas articulares:", padx=0, pady=0).place(height=225, width=170, x=450, y=10)
data_pos_q1 = tk.StringVar()
entry_pos_q1 = Entry(frame1).place(height=25, width=35, x=540, y=40)
lab_pos_q1 = Label(frame1, text="Cintura:").place(x=460, y=40)
data_pos_q2 = tk.StringVar()
entry_pos_q2 = Entry(frame1).place(height=25, width=35, x=540, y=80)
lab_pos_q2 = Label(frame1, text="Hombro:").place(x=460, y=80)
data_pos_q3 = tk.StringVar()
entry_pos_q3 = Entry(frame1).place(height=25, width=35, x=540, y=120)
lab_pos_q3 = Label(frame1, text="Codo:").place(x=460, y=120)
data_pos_q4 = tk.StringVar()
entry_pos_q4 = Entry(frame1).place(height=25, width=35, x=540, y=160)
lab_pos_q4 = Label(frame1, text="Muñeca:").place(x=460, y=160)
go1 = Button(frame1, text="Ir", bg="Yellow Green").place(x=520, y=200)

#COORDENADAS CARTESIANAS
ir_a2 = LabelFrame(frame1, text="Ir a coordenadas cartesianas: ", padx=0, pady=0).place(height=180, width=170, x=450, y=245)
lab_pos_x = Label(frame1, text="Posición X:").place(x=460, y=270)
data_pos_x = tk.StringVar()
entry_pos_x = Entry(frame1).place(height=25, width=35, x=540, y=270)
#pos_x = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=260)
#entry_pos_x = ttk.Entry(pos_x, textvariable=data_pos_x)
lab_pos_y = Label(frame1, text="Posición Y:").place(x=460, y=310)
data_pos_y = tk.StringVar()
entry_pos_y = Entry(frame1).place(height=25, width=35, x=540, y=310)
#pos_y = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=300)
#entry_pos_y = ttk.Entry(pos_y, textvariable=data_pos_y)
lab_pos_z = Label(frame1, text="Posición Z:").place(x=460, y=350)
data_pos_z = tk.StringVar()
entry_pos_z = Entry(frame1).place(height=25, width=35, x=540, y=350)
#pos_z = Frame(bd=1, relief="groove", background="white").place(height=25, width=35, x=540, y=340)
#entry_pos_z = ttk.Entry(pos_z, textvariable=data_pos_z)
go2 = Button(frame1, text="Ir", bg="Yellow Green").place(x=520, y=390)

# ARTICULACIONES
marco2 = LabelFrame(frame1, text="Movimiento Articulaciones: ", padx=0, pady=0).place(height=360, width=230, x=210, y=10)

# INFORMACIÓN SERVOMOTORES

lab_q1 = Label(frame1, text="Q1: 180º").place(x=250, y=30)
lab_q2 = Label(frame1, text="Q2: 90º").place(x=250, y=60)
lab_q3 = Label(frame1, text="Q3: -90º").place(x=350, y=30)
lab_q4 = Label(frame1, text="Q4: 180").place(x=350, y=60)

# ARTICULACIÓN 1
var1 = DoubleVar
cintura = Scale(frame1, variable=var1, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
                troughcolor='gray', highlightcolor='white', label='Cintura(Q1)')
cintura.set(0)  # pos home dexarm (AÑADIR)
cintura.place(x=220, y=90)

# ARTICULACIÓN 2
var2 = DoubleVar
hombro = Scale(frame1, variable=var2, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
               troughcolor='gray', highlightcolor='white', label='Hombro(Q2)')
hombro.set(0)  # pos home dexarm (AÑADIR)
hombro.place(x=220, y=150)

# ARTICULACIÓN 3
var3 = DoubleVar
codo = Scale(frame1, variable=var3, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
             troughcolor='gray', highlightcolor='white', label='Codo(Q3)')
codo.set(0)  # pos home dexarm (AÑADIR)
codo.place(x=220, y=220)

# ARTICULACIÓN 4
var4 = DoubleVar
muñeca = Scale(frame1, variable=var4, orient=HORIZONTAL, from_=0, to=180, length=200, width=20, cursor='dot',
               troughcolor='gray', highlightcolor='white', label='Muñeca(Q4)')
muñeca.set(0)  # pos home dexarm (AÑADIR)
muñeca.place(x=220, y=280)

# velocidad.bind("<<ComboboxSelected>>", selection_changed)
# selección velocidad
# def selection_changed(event):
# selection = velocidad.get()
# messagebox.showinfo(tittle="Nuevo elemento seleccionado", message=selection)

marco_vel = LabelFrame(frame1, text="Velocidad: ", padx=0, pady=0).place(height=50, width=165, x=242.5, y=380)
velocidad = ttk.Combobox(frame1, values=["Lenta", "Rápida"]).place(x=252.5, y=400)

# TRAYECTORIAS
marco_movs = LabelFrame(frame2, text="Trayectorias: ", padx=0, pady=0).place(height=250, width=150, x=10, y=190)

# MOVIMIENTO LINEAL
def openwindow1():
    window1 = Toplevel(frame2)
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

movlineal = Button(frame2, text="Movimiento Lineal", height=1, width=15, bg="khaki", command = openwindow1).place(x=20, y=265)
movlineal_frame = Frame(frame2, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=265)

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
    window2 = Toplevel(frame2)
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

movcirc = Button(frame2, text="Movimiento Circular", height=1, width=15, bg="khaki", command = openwindow2).place(x=20, y=305)
movcirc_frame = Frame(frame2, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=305)

# CUADRADO
def openwindow3():
    window3 = Toplevel(frame2)
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

cuadrado = Button(frame2, text="Cuadrado", height=1, width=15, bg="khaki", command = openwindow3).place(x=20, y=345)
cuadrado_frame = Frame(frame2, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=345)

# CÍRCULO
def openwindow4():
    window4 = Toplevel(frame2)
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

circulo = Button(frame2, text="Círculo", height=1, width=15, bg="khaki", command = openwindow4).place(x=20, y=385)
circulo_frame = Frame(frame2, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=385)

# CALIBRACIÓN
def openwindow5():
    window5 = Toplevel(frame2)
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

calibracion = Button(frame2, text="Calibración", height=1, width=15, bg="khaki", command=openwindow5).place(x=20, y=225)
calibracion_frame = Frame(frame2, bd=1, relief="groove", background="white").place(height=25, width=35, x=165, y=225)

# POSICIÓN ACTUAL
pos = LabelFrame(frame1, text="Posición actual", padx=0, pady=0).place(height=70, width=610, x=10, y=440)
pos_x1 = Label(frame1, text='Eje X').place(x=35, y=470)
marco_posx = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=70, y=470)
pos_y1 = Label(frame1, text='Eje Y').place(x=115, y=470)
marco_posy = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=150, y=470)
pos_z1 = Label(frame1, text='Eje Z').place(x=195, y=470)
marco_posz = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=230, y=470)
pos_q1 = Label(frame1, text='Q1').place(x=275, y=470)
marco_posq1 = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=310, y=470)
pos_q2 = Label(frame1, text='Q2').place(x=355, y=470)
marco_posq2 = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=390, y=470)
pos_q3 = Label(frame1, text='Q3').place(x=435, y=470)
marco_posq3 = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=470, y=470)
pos_q4 = Label(frame1, text='Q4').place(x=515, y=470)
marco_posq4 = Frame(frame1, bd=1, relief="groove", background="white").place(height=25, width=35, x=550, y=470)

# bucle principal, no finaliza hasta cerrar la última ventana de la aplicación
root.mainloop()