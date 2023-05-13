import pandas as pd
import numpy as np

import sympy as sp

df = pd.read_csv("Tabla.csv", sep=';', index_col=0)

#beta = ys, lam, alpha = [12.9,13.27,1.88]
#theta = gama0, gama1, gama2, delta0, delta1 = [0.1, 0.1, 0.1, 0.1, 0.1]
beta = ys, lam, alpha = sp.symbols('ys, lam, aplha')
theta = gama0, gama1, gama2, delta0, delta1 = sp.symbols('gama0, gama1, gama2, delta0, delta1')

h = df[['h']].values
t = df[['t']].values
y = df[['y']].values
ye = df[['ye']].values

T = len(h)

def get_sigma2():
    f = lambda i, j: sp.exp(gama0 + gama1 * h[i][0] + gama2 * (h[i][0]**2))
    sigma2 = sp.Matrix(T, 1, f)

    return sigma2

sigma2 = get_sigma2()

def get_PSI():
    f = lambda i, j: (delta0 - delta1 * abs(h[i][0] - h[j][0])) * sp.sqrt(sigma2[i] * sigma2[j]) if t[i] == t[j]  else 0
    PSI = sp.Matrix(T, T, f)

    return PSI

PSI = get_PSI()
input(sp.det(PSI))

def get_w():
    f = lambda i, j: 1 - (1 / sp.exp((h[i][0]/lam)**alpha))
    w = sp.Matrix(1, T, f)

    return w

w = get_w()

def get_PHI():
    f = lambda i, j : w[i] * ys + (1 - w[i]) * y[i][0]
    PHI = sp.Matrix(T, 1, f)

    return PHI

PHI = get_PHI()

def get_fl():
    f = -(T/2) * sp.log(2 * sp.pi) - (1/2) #* sp.det(PSI) - (1/2) #* dot(dot(transpose((ye - PHI)), inv(PSI)).flatten(), (ye - PHI))
    return f

fl = get_fl()

print(fl)
