import math

import fontTools.misc.plistlib
import numpy
import numpy as np
import sympy
import sympy as sym

#definición variables

l1, l2, l3 = 4, 15, 17
l4: float = 4.5
x, y, z = 0, 0, 0
div1 = 0
x_max, y_max, z_max = 284, 414, 168
x_min, y_min, z_min = -283, 186, -127
d1 = l1
d2, d3, d4 = 0, l3, 0
a1 = 0
a2 = l2
a3 = 0
a4 =0
qd, q1, q2, q3, q4 = 0, 0, 0, 0, 0
alfa1_rad = (math.pi) / 2
alfa1 = math.degrees(alfa1_rad)
alfa2_rad, alfa3_rad = 0, 0
alfa4_rad = math.pi/2

print("Valores coordenadas: ")
x = float(input())
y = float(input())
z = float(input())
print(x, y, z)

while (float(x) >= x_max or float(y) >= y_max or float(z) >= z_max):
    print("Valores fuera de rango")
    print("Valores coordenadas: ")
    x = float(input())
    y = float(input())
    z = float(input())
else:

    #primera función geométrica
    #r1 = math.sqrt(pow(x, 2) + pow(y, 2))
    #sin1 = y / r1
    #cos1 = x / r1
    #q1rad = math.atan2(sin1, cos1)
    #q1 = math.degrees(q1rad)
    #print("q1rad:", q1rad)
    #print("q1:", q1)

    #tercera función geométrica
    #cos3 = (pow(x, 2) + pow(y, 2) + pow(z, 2) - pow(l2, 2) - pow(l3, 2)) / (2 * l2 * l3)
    #print("cos3: ", cos3)
    #sen3 = math.sqrt(abs(1 - pow(cos3, 2)))
    #q31 = math.degrees(math.atan2(sen3, cos3)) #ángulo en grados
    #q32 = (-1) * math.degrees(math.atan2(sen3, cos3)) #ángulo en graods
    #q3rad = math.atan2(sen3, cos3) #ángulo en radianes
    #print("q3rad: ", q3rad)
    #print("q31: ", q31)
    #print("q32: ", q32)

    #segunda función geométrica --> NO DA VALOR
    #r2 = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z - l1, 2))
    #cos_beta = (pow(l3, 2) - pow(r2, 2) + pow(l2, 2)) / ((-1) * 2 * r2 * l2)
    #sin_beta = math.sqrt(1 - pow(cos_beta, 2))
    #cos_alfa = r1 / r2
    #sin_alfa = (l1 - z) / r2
    #beta = math.atan2(sin_beta, cos_beta)
    #alfa = math.atan2(sin_alfa, cos_alfa)
    # codo arriba
    #q2r_rad = alfa + beta
    #print("q2 codo arriba radianes: ", q2r_rad)
    #q2r = math.degrees(q2r_rad)
    #print("q2 codo arriba grados: ", q2r)
    # codo abajo
    #q2j_rad = alfa - beta
    #print("q2 codo abajo radianes: ", q2j_rad)
    #q2j = math.degrees(q2j_rad)
    #print("q2 codo abajo grados: ", q2j)
    #c3 = (pow(x, 2)+pow(y, 2)+pow(z, 2)-pow(a2, 2)-pow(a3, 2))/2*a2*a3
    #s3 = math.sqrt(math.fabs(1-pow(c3, 2)))
    #c2 = (math.sqrt(pow(x, 2)+pow(y, 2))*(a2+a3*c3)+(z*a3*s3))/pow(a2, 2)+pow(a3, 2)+(2*a2*a3*c3)
    #s2 =(z*(a2+a3*c3)+math.sqrt(pow(x, 2)+pow(y, 2))*a3*s3)/pow(a2, 2)+pow(a3, 2)+(2*a2*a3*c3)
    #q2rad = math.atan2(s2, c2)
    #q2deg = math.degrees(q2rad)
    #print("q2deg:", q2deg)

    #cinemática directa
    q1d = float(input("Ángulo 1 en grados:"))
    q1d_rad = math.radians(q1d)
    q2d = float(input("Ángulo 2 en grados:"))
    q2d_rad = math.radians(q2d)
    q3d = float(input("Ángulo 3 en grados:"))
    q3d_rad = math.radians(q3d)
    #q4d = float(input("Ángulo 4 en grados:"))
    #q4d_rad = math.radians(q4d)

    q4d = 90
    q4d_rad = math.radians(q4d)

    #Matriz de transformación de la Base
    A01 = np.array([[math.cos(q1d_rad), (-1)*math.sin(q1d_rad)*math.cos(alfa1_rad), math.sin(q1d_rad)*math.sin(alfa1_rad), a1*math.cos(q1d_rad)],
                    [math.sin(q1d_rad), math.cos(q1d_rad)*math.cos(alfa1_rad), (-1)*math.sin(alfa1_rad)*math.cos(q1d_rad), a1*math.sin(q1d_rad)],
                    [0, math.sin(alfa1_rad), math.cos(alfa1_rad), d1],
                    [0, 0, 0, 1]])
    print("A01=", A01)
    #Matriz de transformación del Brazo
    A12 = np.array([[math.cos(q2d_rad), (-1)*math.sin(q2d_rad)*math.cos(alfa2_rad), math.sin(q2d_rad)*math.sin(alfa2_rad), a2*math.cos(q2d_rad)],
                    [math.sin(q2d_rad), math.cos(q2d_rad)*math.cos(alfa2_rad), (-1)*math.sin(alfa2_rad)*math.cos(q2d_rad), a2*math.sin(q2d_rad)],
                    [0, math.sin(alfa2_rad), math.cos(alfa2_rad), d2],
                    [0, 0, 0, 1]])
    print("A12=", A12)
    #Matriz de transformación del Antebrazo
    A23 = np.array([[math.cos(q3d_rad), (-1)*math.sin(q3d_rad)*math.cos(alfa3_rad), math.sin(q3d_rad)*math.sin(alfa3_rad), a3*math.cos(q3d_rad)],
                    [math.sin(q3d_rad), math.cos(q3d_rad)*math.cos(alfa3_rad), (-1)*math.sin(alfa3_rad)*math.cos(q3d_rad), a3*math.sin(q3d_rad)],
                    [0, math.sin(alfa3_rad), math.cos(alfa3_rad), d3],
                    [0, 0, 0, 1]])
    print("A23=", A23)
    #Matriz de transformación de la Muñeca
    A34 = np.array([[math.cos(q4d_rad), (-1)*math.sin(q4d_rad)*math.cos(alfa4_rad), math.sin(q4d_rad)*math.sin(alfa4_rad), a4*math.cos(q4d_rad)],
                    [math.sin(q4d_rad), math.cos(q4d_rad)*math.cos(alfa4_rad), (-1)*math.sin(alfa4_rad)*math.cos(q4d_rad), a4*math.sin(q4d_rad)],
                    [0, math.sin(alfa4_rad), math.cos(alfa4_rad), d4],
                    [0, 0, 0, 1]])
    print("A34=", A34)
    #Matriz de transformación homogénea Base-Muñeca
    A02 = np.dot(A01, A12)
    print("A02=", A02)
    A03 = np.dot(A02, A23)
    print("A03=", A03)
    A04 = np.dot(A03, A34)
    print("A04=", A04)

    #prueba q4

    #q4_prueba = 0 - q2deg - q31
    #print("q4prueba:", q4_prueba)

    #cuarta función geométrica
    #C = A03[2][2]*A34[2][3]
    #D = A03[2][3]*A34[3][3]
    #A = A03[2][0]*l2
    #B = A03[2][1]*l4
    #E = z - C - D
    #num1 = (-1)*2*E*B
    #num2 = pow(((-1)*2*E*B), 2)
    #num3 = 4*((-1)*pow(A, 2) - pow(B, 2))*(pow(A, 2)-pow(E, 2))
    #den1 = 2*((-1)*pow(A, 2)-pow(B, 2))
    #senx1 = (num1 + math.sqrt(math.fabs(num2-num3))) / den1
    #senx2 = (num1 - math.sqrt(math.fabs(num2-num3))) / den1
    #x1rad = math.asin(senx1)
    #print("x1rad:", x1rad)
    #x1deg = math.degrees(x1rad)
    #print("x1deg:", x1deg)
    #x2rad = math.asin(senx2)
    #print("x2rad:", x2rad)
    #x2deg = math.degrees(x2rad)
    #print("x2deg:", x2deg)

    #coordenadas de la base
    #Matriz de transformación homogénea Muéca-Base (Matrices inversas)
    #A40 = np.dot(np.linalg.inv(A34), np.linalg.inv(A23))
    #print("A40=", A40)
    #A30 = np.dot(A40, np.linalg.inv(A12))
    #print("A30=", A30)
    #A20 = np.dot(A30, np.linalg.inv(A01))
    #print("A20=", A20)


    #inversa = np.linalg.inv(A02)
    #identidad = np.dot(A02, inversa)
    #print("identidad =", identidad)

