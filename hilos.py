from multiprocessing.pool import ThreadPool
from t3 import get_simetrica
from matriz import get_det

A = get_simetrica(8)

def square(x):
    i, j = x
    return get_det(A)

if __name__ == '__main__':
    numbers = [[i, j] for i in range(8) for j in range(8)]
    pool = ThreadPool()
    squared_numbers = pool.map(square, numbers)
    pool.close()
    pool.join()
    print(len(squared_numbers))
