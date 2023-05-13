import pandas as pd
from math import pi
from numpy.linalg import inv
from numpy import transpose, exp, log, float64, zeros, dot, gradient

from mpmath import mp, mpf, sqrt, det

from sympy import symbols, diff

df = pd.read_csv("Tabla.csv", sep=';', index_col=0)

beta = ys, lam, alpha = [12.9,13.27,1.88]
gama0, gama1, gama2, delta0, delta1  = theta = [0.1,
                                                0.1,
                                                0.1,
                                                0.1,
                                                0.1]

def l(beta, X, h, T, ye, t, y):
    gama0, gama2, gama1 = [0.1,0.1,0.1]
    
    sigma2 = zeros((T, 1))

    for i in range(T):
        try: 
            sigma2[i] = exp(gama0 + gama1 * h[i] + gama2 * (h[i]**2))
        
        except:
            exponente = gama0 + gama1 * h[i] + gama2 * (h[i]**2)
            mp.dps = 50 

            sigma2[i] = int(mp.exp(exponente))

    PSI = zeros((T, T)).astype(float64)
    PHI = zeros((T, 1))

    for i in range(T):
        for j in range(T):
            if t[i] == t[j]:    
                mp.dps = 100 
                sigma2_i = mpf(sigma2[i][0])
                sigma2_j = mpf(sigma2[j][0])

                raices = sqrt(sigma2_i * sigma2_j)
                PSI[i][j] = (delta0 - delta1 * abs(h[i] - h[j])) * raices

            else:
                PSI[i][j] = 0.0

    def w (T, h, lam, alpha):
        W = [int() for i in range(T)]

        for i in range(T):
            W[i] = 1 - (1 / exp((h[i]/lam)**alpha))

        return W

    for i in range(T):
        PHI[i] = w(T, h, lam, alpha)[i] * ys + (1 - w(T, h, lam, alpha)[i]) * y[i]

        
    PSI = PSI.astype(float64)
    fl = -(T/2) * log(2 * pi) - (1/2) * det(PSI) - (1/2) * dot(dot(transpose((ye - PHI)), inv(PSI)).flatten(), (ye - PHI))


    input(fl)
    return fl

def v2 ():

    sigma2 = zeros((T, 1))
    print(sigma2)

v2()

h = df[['h']].values.astype(float64)
T = len(h)
t = df[['t']].values
y = df[['y']].values
ye = df[['ye']].values
"""
l(
    beta=0,
    X=0,
    h=h,
    T=T,
    ye=ye,
    t=t,
    y=y
)"""