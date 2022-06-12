# Matriz de transformación de la Base
A01 = np.array([[math.cos(q1d), 0, math.sin(q1d), 0],
                [math.sin(q1d), 0, (-1) * math.cos(q1d), 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1]])
print("A01=", A01)
# Matriz de transformación del Brazo
A12 = np.array([[math.cos(q2d), (-1) * math.sin(q2d), 0, a2 * math.cos(q2d)],
                [math.sin(q2d), math.cos(q2d), 0, a2 * math.sin(q2d)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A12=", A12)
# Matriz de transformación del Antebrazo
A23 = np.array([[math.cos(q4d), (-1) * math.sin(q4d), 0, a4 * math.cos(q4d)],
                [math.sin(q4d), math.cos(q4d), 0, a4 * math.sin(q4d)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A23=", A23)

# Matriz de transformación de la Muñeca
A34 = np.array([[math.cos(q3d), (-1) * math.sin(q3d), 0, a3 * math.cos(q3d)],
                [math.sin(q3d), math.cos(q3d), 0, a3 * math.sin(q3d)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print("A23=", A34)

# Matriz de transformación de la Muñeca
# A34 = np.array([[math.cos(q4d), 0, math.sin(q4d), 0],
#                    [math.sin(q4d), 0, (-1)*math.cos(q4d), 0],
#                    [0, 1, 0, 0],
#                    [0, 0, 0, 1]])
# print("A34=", A34)

Rz = np.array([[math.cos(q4d), (-1) * math.sin(q4d), 0],
               [math.sin(q4d), math.cos(q4d), 0],
               [0, 0, 1]])
print("Rz: ", Rz)
Rz_inv = np.linalg.inv(Rz)

Ry = np.array([[math.cos(q4d), 0, math.sin(q4d)],
               [0, 1, 0],
               [math.sin(q4d), 0, math.cos(q4d)]])

Rx = np.array([[1, 0, 0],
               [0, math.cos(q4d), (-1) * math.sin(q4d)],
               [0, math.sin(q4d), math.cos(q4d)]])

# Matriz de transformación homogénea Base-Muñeca
A02 = np.dot(A01, A12)
print("A02=", A02)
A03 = np.dot(A02, A23)
print("A03=", A03)
A04 = np.dot(A03, A34)
print("A04: ", A04)

R_rot = np.dot(Rx, Ry, Rz)
print("Rrotacion: ", R_rot)

array_x = np.array([[A03[0][3]],
                    [0],
                    [0]])

array_y = np.array([[0],
                    [A03[1][3]],
                    [0]])

array_z = np.array([[0],
                    [0],
                    [A03[2][3]]])

coordenadas = np.array([[A03[0][3]],
                        [A03[1][3]],
                        [A03[2][3]]])

final1 = np.dot(Rz, Ry, Rx)
final = np.dot(final1, coordenadas)
print("final: ", final)