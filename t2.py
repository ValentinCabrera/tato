import sympy as sp
import time
from economia.main_v2 import get_PSI

def calc_det(matriz):
    inicio = time.time()
    det = sp.det(matriz)
    fin = time.time()

    print(fin-inicio)
    print(det)

def m1():
    variables = [sp.symbols(f'_{i}') for i in range(16)]
    m = sp.Matrix(4,4, variables)
    calc_det(m)

def m2():
    n = 3

    variables = [sp.symbols(f'_{i}') for i in range(int((n*(n - 1)/ 2) + n))]
    simetrica = [[int(0) for j in range(n)] for i in range(n)]

    last = n - 1

    for i in range(n):
        for j in range(n):
            if i == j:
                simetrica[i][j] = variables[i]

            elif j > i:
                last += 1
                simetrica[i][j] = variables[last]
                simetrica[j][i] = variables[last]

    m = sp.Matrix(n, n, lambda i, j: simetrica[i][j])



x = [[2,4,5,6],
     [4,6,7,8],
     [0,7,8,4],
     [1,2,1,9]]

m = sp.Matrix(4,4, lambda i,j: x[i][j])
A = sp.Matrix(2,2, [x[0][0], x[0][1], x[1][0], x[1][1]])
B = sp.Matrix(2,2, [x[0][2], x[0][3], x[1][2], x[1][3]])
C = sp.Matrix(2,2, [x[2][0], x[2][1], x[3][0], x[3][1]])
D = sp.Matrix(2,2, [x[2][2], x[2][3], x[3][2], x[3][3]])

mm = sp.Matrix(2,2, [A, B, C, D])
res = sp.det(A)*sp.det(D-(C*A.inv()*B))


"""
    0    1    2    3

0   _0   _1   _2   _3
1   _4   _5   _6   _7
2   _8   _9   _10  _11
3   _12  _13  _14  _15

"""


"""
simetrica

     0  1  2  3

0    00 01 02 03
1    01 04 05 06
2    02 05 07 08
3    03 06 08 09

numero de ecuaciones = n*(n - 1)/ 2) + n
"""