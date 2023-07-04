from main import PSI
from default_det_calculator import get_det

from time import time
import sympy as sp
from multiprocessing import Pool
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args):
        inicio = time()
        print("Calculando")
        func(*args)
        fin = time()

        print(fin - inicio)

    return wrapper

@decorator
def test(func, symbol):
    sp.diff(func, sp.symbols(symbol))

if __name__ == "__main__":
    pool = Pool(processes=8)

    det_PSI = get_det(PSI)

    results = [pool.apply_async(test, args=(det_PSI.args[i], "gama0",)) for i in range(48)]

    pool.close()
    pool.join()

    outputs = [result.get() for result in results]
