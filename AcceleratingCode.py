from numba import cuda, jit, njit, vectorize
from matplotlib import pyplot as plt

def mandel(x, y, max_iters):

    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iters
