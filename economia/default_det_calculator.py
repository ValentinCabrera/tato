import sympy as sp

def get_det(array):
    n = int(len(array)**(1/2))

    M = sp.Matrix(n, n, [array[i] for i in range(n*n)])
    L = M.LUdecomposition()
    L = L[1]

    expr = 1

    for i in range(sp.shape(L)[0]):
        for j in range(sp.shape(L)[1]):
            if i == j:
                expr *= L[i, j]

    return expr

if __name__ == "__main__":
    pass
