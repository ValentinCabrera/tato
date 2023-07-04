import sympy as sp

def get_simetrica(n=3):
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

    return sp.Matrix(n, n, lambda i, j: simetrica[i][j])

def get_simbolica(n=3):
    variables = [sp.symbols(f'_{i}') for i in range(n*n)]
    simbolica = [int(0) for j in range(n*n)]

    for i in range(n*n):
        simbolica[i] = variables[i]

    return sp.Matrix(n, n, simbolica)

def get_random(n=3):
    from random import randint
    return sp.Matrix(n,n, [randint(1,50) for i in range(n*n)])