import sympy as sp
import time

from economia.main_v2 import get_PSI, gama0, gama1, gama2, delta0, delta1


dimension = [int(i) for i in range(2)]

PSI = get_PSI()#.extract(dimension, dimension)

def get_mm(m):
    sub_matriz = lambda i, j: sp.Matrix(2, 2, [PSI[i * 2, j * 2], PSI[i * 2, j * 2 + 1], PSI[i * 2 + 1, j * 2], PSI[i * 2 + 1, j * 2 + 1]])
    mm = sp.Matrix(2, 2, sub_matriz)
    return mm

mm = get_mm()
md = sp.Matrix(2, 2, lambda i, j: sp.det(mm[i, j]))

print(md)


