import pandas as pd
import sympy as sp

df = pd.read_csv("Tabla.csv", sep=';', index_col=0)

h = df[['h']].values
t = df[['t']].values
y = df[['y']].values
ye = df[['ye']].values

T = len(h)