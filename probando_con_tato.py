import sympy as sp
from t3 import get_simetrica

"""A = sp.Matrix(2,2, [1,2,8,2])
B = sp.Matrix(2,2, [8,3,8,2])
C = sp.Matrix(2,2, [6,8,3,0])
D = sp.Matrix(2,2, [0,5,1,6])
E = sp.Matrix(2,2, [2,7,9,4])
F = sp.Matrix(2,2, [7,3,8,2])
G = sp.Matrix(2,2, [6,7,1,0])
H = sp.Matrix(2,2, [1,5,5,7])
I = sp.Matrix(2,2, [8,4,6,3])

M = sp.Matrix(6,6, [1,2,8,3,6,8,
                    8,2,8,2,3,0,
                    0,5,2,7,7,3,
                    1,6,9,4,8,2,
                    6,7,1,5,8,4,
                    1,0,5,7,6,3])"""

from economia.main_v2 import get_PSI
M = get_PSI().extract([0,1,2,3,4,5], [0,1,2,3,4,5])#get_simetrica(6)

A = sp.Matrix(2,2, [M[0,0],M[0,1],M[1,0],M[1,1]])
B = sp.Matrix(2,2, [M[0,2],M[0,3],M[1,2],M[1,3]])
C = sp.Matrix(2,2, [M[0,4],M[0,5],M[1,4],M[1,5]])
D = sp.Matrix(2,2, [M[2,0],M[2,1],M[3,0],M[3,1]])
E = sp.Matrix(2,2, [M[2,2],M[2,3],M[3,2],M[3,3]])
F = sp.Matrix(2,2, [M[2,4],M[2,5],M[3,4],M[3,5]])
G = sp.Matrix(2,2, [M[4,0],M[4,1],M[5,0],M[5,1]])
H = sp.Matrix(2,2, [M[4,2],M[4,3],M[5,2],M[5,3]])
I = sp.Matrix(2,2, [M[4,4],M[4,5],M[5,4],M[5,5]])

from time import time

def sarrus2x2(A):
    return A[0,0] * A[1,1] - A[0,1] * A[1,0]

inicio = time()

Ainv = A.adjoint() / sarrus2x2(A)
X = E-D*Ainv*B
print("Se calculo X")

Xinv = X.adjoint() / sarrus2x2(X)
Ainv_por_C = Ainv*C

Z = I-G*Ainv_por_C-(H-G*Ainv*B)*Xinv*(F-D*Ainv_por_C)
print("Se calculo Z")
a_det = A[0,0] * A[1,1] - A[0,1] * A[1,0]
print("Se calculo DET A")
x_det = X[0,0] * X[1,1] - X[0,1] * X[1,0]
print("Se calculo DET X")
z_det = Z[0,0] * Z[1,1] - Z[0,1] * Z[1,0]
print("Se calculo DET Z")
res = a_det * x_det * z_det
fin = time()

print(fin-inicio)

"""M = get_simetrica(6)

A = sp.Matrix(3,3, [M[0,0],M[0,1],M[0,2], M[1,0], M[1,1], M[1,2], M[2,0], M[2,1], M[2,2]])
B = sp.Matrix(3,3, [M[0,3],M[0,4],M[0,5], M[1,3], M[1,4], M[1,5], M[2,3], M[2,4], M[2,5]])
C = sp.Matrix(3,3, [M[3,0],M[3,1],M[3,2], M[4,0], M[4,1], M[4,2], M[5,0], M[5,1], M[5,2]])
D = sp.Matrix(3,3, [M[3,3],M[3,4],M[3,4], M[4,3], M[4,4], M[4,5], M[5,3], M[5,4], M[5,5]])

c = A*D-(A*C*A.inv()*B)
print(len(c))
"""