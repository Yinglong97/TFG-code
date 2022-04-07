import math
import numpy
import numpy as np
import sympy
import sympy as sym

#definición variables
l1, l2 , l3 = 5, 10, 10
l4: float = 5
x, y, z = 0, 0, 0
div1 = 0
x_max, y_max, z_max = 40, 40, 40
d1 = 5
qd = 0

print("Introduce los valores de los ejes de coordenadas: ")
x = input()
y = input()
z = input()

print(x, y, z)

while (float(x) >= x_max or float(y) >= y_max or float(z) >= z_max):
    print("Valores fuera de rango")
    print("Introduce los valores de los ejes de coordenadas: ")
    x = input()
    y = input()
    z = input()
else:
    div1 = (float(y) / float(x))

    q1rad = math.atan(div1) #valor del arcotangente en radianes
    q1 = (q1rad*180) / math.pi #radianes a grados
    print("q1rad:", q1rad)
    print("q1:", q1)

    #tercera función geométrica
    #potencias
    pox = pow(float(x), 2)
    poy = pow(float(y), 2)
    poz = pow(float(z), 2)
    pol2 = pow(float(l2), 2)
    pol3 = pow(float(l3), 2)
    pol1 = pow(float(l1), 2) #definir función para potencias de un vector

    frac_cos = (pox + poy + poz - pol2 - pol3) / (2 * l2 * l3)
    cos3 = math.atan(frac_cos)
    print(cos3)

    int_cos = math.acos(cos3)
    sen3 = math.sin(int_cos)

    cos3cuad = pow(cos3, 2)
    r = 1 - cos3cuad
    num3 = math.sqrt(r)
    div3 = num3 / cos3

    q3 = ((math.atan(div3))*180) / math.pi #ángulo en grados
    q3rad = math.atan(div3) #ángulo en radianes
    print("q3rad:", q3rad)
    print("q3:", q3)
    #print(q3rad)

#segunda función geométrica
    d = pow(float(x), 2) + pow(float(y), 2)
    den21 = math.sqrt(d)
    den22 = l2 + (l3 * cos3)
    num2 = l3 * sen3
    frac1 = float(z) / den21
    frac2 = num2 / den22
    q2rad = (math.atan(frac1)) - (math.atan(frac2))
    print("q2rad:", q2rad)
    q2 = (q2rad*180) / math.pi
    print("q2:", q2)

#cuarta función geométrica

    q4i = qd + q2 + q3
    print("q4i: ", q4i)

#cinemática directa

q1d = float(input("Ángulo 1 en grados:"))
q1d_rad = math.radians(q1d)
q2d = float(input("Ángulo 2 en grados:"))
q2d_rad = math.radians(q2d)
q3d = float(input("Ángulo 3 en grados:"))
q3d_rad = math.radians(q3d)
q4d = float(input("Ángulo 4 en grados:"))
q4d_rad = math.radians(q4d)

alfa1rad = (math.pi) / 2
alfa1 = (alfa1rad*180) / math.pi

#Matriz de transformación de la Base
A01 = np.array([[math.cos(q1d_rad), 0, math.sin(math.pi/2)*math.sin(q1d_rad), 0],
                [math.sin(q1d_rad), 0, (-1)*math.sin(math.pi/2)*math.cos(q1d_rad), 0],
                [0, 1, 0, d1],
                [0, 0, 0, 1]])
print("A01=", A01)

#Matriz de transformación del Brazo
A12 = np.array([[math.cos(q2d_rad), (-1)*math.sin(q2d_rad), 0, l2*math.cos(q2d_rad)],
                [math.sin(q2d_rad), math.cos(q2d_rad), 0, l2*math.sin(q2d_rad)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A12=", A12)

#Matriz de transformación del Antebrazo
A23 = np.array([[np.cos(q3d_rad), (-1)*np.sin(q3d_rad), 0, l3*np.cos(q3d_rad)],
                [np.sin(q3d_rad), np.cos(q3d_rad), 0, l3*np.sin(q3d_rad)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A23=", A23)

#Matriz de transformación de la Muñeca
A34 = np.array([[np.cos(q4d_rad), (-1)*np.sin(q4d_rad), 0, l2*np.cos(q4d_rad)],
                [np.sin(q4d_rad), np.cos(q4d_rad), 0, l4*np.sin(q4d_rad)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A34=", A34)

A02 = np.dot(A01, A12)
A03 = np.dot(A02, A23)
print("A03=", A03)
A04 = np.dot(A03, A34)
print("A04=", A04)

#cuarta función geométrica

C = A03[2][2]*A34[2][3]
D = A03[2][3]*A34[3][3]
A = A03[2][0]*l2
B = A03[2][1]*l4
ang = math.atan(A/B)
arg = (pow(A, 2))+(pow(B, 2))
R = pow(arg, 0.5)
num4: float = (float(z) - C - D)*float(R)
frac4 = num4/arg
resfrac4 = sympy.asin(frac4)
q4radi = resfrac4 - ang
print("q4rad:", q4radi)
q4 = (q4radi*180) / math.pi
print("q4:", q4)
#Hola