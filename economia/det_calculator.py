import sympy as sp
from multiprocessing.pool import ThreadPool

def get_dim(A):
    """
    calcula en cuantos sub bloques se puede dividir en base a las formulas de determinantes que tenemos

    args = 1 | A = sp.Matrix a dividir

    retorna: cantidad de sub bloques
        | en caso de tener dimension 1, retorna none

    Si devuelve True, se debe calcular el determinante
    Si devuelve False, se debe calcular por bloques

    """

    from pkl_to_expr import get_default_symbols
    
    dim = 1
    default_det = get_default_symbols()

    while dim <= sp.shape(A)[0]:
        if sp.shape(A)[0] % dim == 0 and sp.shape(A)[0] / dim in default_det:
            if dim == 1:
                return int(sp.shape(A)[0] / dim), True
            
            return int(sp.shape(A)[0] / dim), False
        
        dim += 1

    return None, True

def get_blocks_det(A, dim):
    """
    devuelve la matriz dividida en sub bloques de la dimension pasada por parametro
    cada bloque es una sp.Matrix

    args = 2 
        | A = matriz de tipo sp.Matrix
        | dim = dimension de la matriz dividida

    retorna: matriz sp.Matrix, donde cada elemento de la misma es una sp.Matrix
    
    """

    blocks = []

    n = int(sp.shape(A)[0] / dim)

    for i in range(dim):
        for j in range(dim):
            block = sp.Matrix(n,n, lambda k,l:A[k + i * n,l + j * n])
            blocks.append(block)
    
    return blocks

def commun_det(A, dim):
    from pkl_to_expr import get_symbols_det
    expr = get_symbols_det(dim).as_expr()

    symbols = expr.free_symbols

    dic = {}

    for i in symbols:
        num = int(i.__str__()[2:-1])
        dic[i] = A[num]

    
    res = expr.subs(dic)
    res = res.doit()
    return res

def blocks_det(blocks, dim):
    from pkl_to_expr import get_default_det
    
    expr = get_default_det(dim)
    dic = {}

    n = blocks[0].shape[0]

    for i in range(dim*dim):
        globals()[f'_{i}'] = sp.MatrixSymbol(f'_{i}', n, n)
        globals()[f'_{i}_val'] = blocks[i]

        dic[sp.MatrixSymbol(f'_{i}', n,n)] = blocks[i]

    expresion_evaluada = eval(str(expr))
    res = expresion_evaluada.subs(dic).doit()

    return get_det(res)

def get_det(A):
    """
    si es mayor a 3 por 3:
        - obtiene los bloques en base a su dimension
        - obtiene el determinante por bloques

    si no: lo obtiene de forma directa

    
    args = 1 | objeto sp.Matrix de dimension nxn
    
    retorna: el determinante de la matriz ingresada
    """

    dim, state = get_dim(A)

    if dim:
        if state == True:
            return commun_det(A, dim)
        
        else:
            blocks =  get_blocks_det(A, dim)
            return blocks_det(blocks, dim)
            
    else:
        return A[0]

from array_generator import get_simbolica, get_random
from time import time

i = 2
while i <= 20:
    print(f"{i}X{i}")
    A = get_simbolica(i)
    inicio = time()
    d1 = get_det(A)
    fin = time()
    print(f"Yo: {fin-inicio} \n")

    i += 1


    

