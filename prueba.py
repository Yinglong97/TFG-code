import cmath
import math

import fontTools.misc.plistlib
import numpy
import numpy as np
import sympy
import sympy as sym

# definición variables

l1, l2, l3 = 40, 150, 170
l4: float = 45
div1 = 0
x_max, y_max, z_max = 284, 414, 168
x_min, y_min, z_min = -283, 186, -127
d1 = 0
d2, d3, d4 = 0, 0, 0
a1 = 0
a2 = l2 + l1
a3 = l3
a4 = 0
qd, q1, q2, q3, q4 = 0, 0, 0, 0, 0
alfa1_rad = math.pi / 2
alfa1 = math.degrees(alfa1_rad)
alfa2_rad = 0
alfa2 = math.degrees(alfa2_rad)
alfa3_rad = 0
alfa3 = math.degrees(alfa3_rad)
alfa4_rad = math.pi / 2
alfa4 = math.degrees(alfa4_rad)

# cinemática directa
q1d = float(input("Ángulo 1 en grados:"))
q1d_rad = math.radians(q1d)
q2d1 = float(input("Ángulo 2 en grados:"))
q2d = q2d1 - 90
q2d_rad = math.radians(q2d)
q3d = float(input("Ángulo 3 en grados:"))
q3d_rad = math.radians(q3d)

q4d = q3d
q4d_rad = math.radians(q4d)

# Matriz de transformación de la Base
A01 = np.array([[math.cos(q1d), (-1) * math.sin(q1d) * math.cos(alfa1),
                 math.sin(q1d) * math.sin(alfa1), a1 * math.cos(q1d)],
                [math.sin(q1d), math.cos(q1d) * math.cos(alfa1),
                 (-1) * math.sin(alfa1) * math.cos(q1d), a1 * math.sin(q1d)],
                [0, math.sin(alfa1), math.cos(alfa1), d1],
                [0, 0, 0, 1]])
print("A01=", A01)

# Matriz de transformación del Brazo
A12 = np.array([[math.cos(q2d), (-1) * math.sin(q2d), 0, a2 * math.cos(q2d)],
                [math.sin(q2d), math.cos(q2d), 0, a2 * math.sin(q2d)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A12=", A12)

# Matriz de transformación del Antebrazo
A23 = np.array([[math.cos(q3d), (-1) * math.sin(q3d), 0, a3 * math.cos(q3d)],
                [math.sin(q3d), math.cos(q3d), 0, a3 * math.sin(q3d)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A23=", A23)


A02 = np.dot(A01, A12)
print("A02=", A02)
A03 = np.dot(A02, A23)
print("A03=", A03)


qz = q3d
qy = 90
qx = 90

Rz = np.array([[math.cos(qz), (-1) * math.sin(qz), 0, 0],
               [math.sin(qz), math.cos(qz), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

Ry = np.array([[math.cos(qy), 0, math.sin(qy), 0, 0],
               [0, 1, 0, 0],
               [math.sin(qy), 0, math.cos(qy), 0],
               [0, 0, 0, 1]])

Rx = np.array([[1, 0, 0, 0],
               [0, math.cos(qx), (-1) * math.sin(qx), 0],
               [0, math.sin(qx), math.cos(qx), 0],
               [0, 0, 0, 1]])

array_x = np.array([[A03[0][3]],
                    [0],
                    [0],
                    [1]])

array_y = np.array([[0],
                    [A03[1][3]],
                    [0],
                    [1]])

array_z = np.array([[0],
                    [0],
                    [A03[2][3]],
                    [1]])

coordenadas = np.array([[A03[0][3]],
                        [A03[1][3]],
                        [A03[2][3]],
                        [1]])

rot_1 = np.dot(Rz, Ry)
print("rot_1: ", rot_1)
rot_2 = np.dot(rot_1, Rx)
print("rot_2: ", rot_2)
mat_fin = np.dot(rot_2, coordenadas)
print("mat_fin: ", mat_fin)
