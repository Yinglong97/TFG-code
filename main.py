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
qd, q1, q2, q3, q4 = 0, 0, 0, 0, 0

print("Introduce los valores de los ejes de coordenadas: ")
x = float(input())
y = float(input())
z = float(input())
print(x, y, z)

while (float(x) >= x_max or float(y) >= y_max or float(z) >= z_max):
    print("Valores fuera de rango")
    print("Introduce los valores de los ejes de coordenadas: ")
    x = float(input())
    y = float(input())
    z = float(input())
else:

    #primera función geométrica
    #q1rad = math.atan(y / z) #valor del arcotangente en radianes
    #q1 = math.degrees(q1rad)
    r1 = math.sqrt(pow(x, 2) + pow(y, 2))
    sin1 = y / r1
    cos1 = x / r1
    q1rad = math.atan2(sin1, cos1)
    q1 = math.degrees(q1rad)
    print("q1rad:", q1rad)
    print("q1:", q1)

    #tercera función geométrica
    cos3 = (pow(x, 2) + pow(y, 2) + pow(z, 2) - pow(l2, 2) - pow(l3, 2)) / (2 * l2 * l3)
    sen3 = math.sqrt(abs(1 - pow(cos3, 2)))
    q3 = math.degrees(math.atan2(sen3, cos3)) #ángulo en grados
    q3rad = math.atan2(sen3, cos3) #ángulo en radianes
    print("q3rad:", q3rad)
    print("q3:", q3)

    #segunda función geométrica
    #alfa = math.atan((l3 * sen3) / (l2 + (l3 * cos3)))
    #r = math.sqrt(pow(float(x), 2) + pow(float(y), 2))
    #beta = math.atan(z / r)
    #q2rad = alfa - beta
    #print("q2rad:", q2rad)
    #q2 = math.degrees(q2rad)
    #print("q2:", q2)

    r2 = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z - l1, 2))
    cos_beta = (pow(l3, 2) - pow(r2, 2) + pow(l2, 2)) / ((-1) * 2 * r2 * l2)
    sin_beta = math.sqrt(1 - pow(cos_beta, 2))
    cos_alfa = r1 / r2
    sin_alfa = (l1 - z) / r2
    beta = math.atan2(sin_beta, cos_beta)
    alfa = math.atan2(sin_alfa, cos_alfa)
    # codo arriba
    q2r_rad = alfa + beta
    print("q2 codo arriba radianes: ", q2r_rad)
    q2r = math.degrees(q2r_rad)
    print("q2 codo arriba grados: ", q2r)
    # codo abajo
    q2j_rad = alfa - beta
    print("q2 codo abajo radianes: ", q2j_rad)
    q2j = math.degrees(q2j_rad)
    print("q2 codo abajo grados: ", q2j)

    #tercera función geométrica
    #codo arriba
    q3r_rad = ((3 * math.pi)/2) - beta
    print("q3 codo arriba radianes: ", q3r_rad)
    q3r = math.degrees(q3r_rad)
    print("q3 codo arriba grados: ", q3r)
    #codo abajo
    q3j_rad = beta - (math.pi / 2)
    print("q3 codo abajo radianes: ", q3j_rad)
    q3j = math.degrees(q3j_rad)
    print("q3 codo abajo grados: ", q3j)
    #cuarta función geométrica con ángulo de cabeceo
    #q4i = qd + q2 + q3
    #print("q4i: ", q4i)
    #cinemática directa

    q1d = float(input("Ángulo 1 en grados:"))
    q1d_rad = math.radians(q1d)
    q2d = float(input("Ángulo 2 en grados:"))
    q2d_rad = math.radians(q2d)
    q3d = float(input("Ángulo 3 en grados:"))
    q3d_rad = math.radians(q3d)
    q4d = float(input("Ángulo 4 en grados:"))
    q4d_rad = math.radians(q4d)

    alfa1_rad = (math.pi) / 2
    alfa1 = math.degrees(alfa1_rad)

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
    #Matriz de transformación homogénea Base-Muñeca
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
    resf_rac4 = sympy.asin(frac4)
    q4radi = resf_rac4 - ang
    print("q4rad:", q4radi)
    q4 = math.degrees(q4radi)
    print("q4:", q4)
