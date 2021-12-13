from multiprocessing import *
from time import time
from math import *
from decimal import *

DIGITS = 1500
getcontext().prec = DIGITS
result = []

def calc(n):
    return (Decimal(-1) ** n * factorial(6*n) * (13591409 + 545140134 * n)) / (640320 ** (3 * n + Decimal(3 / 2)) * factorial(3 * n) * factorial(n) ** 3)

if __name__ == '__main__':

    start = time()
    pi = Decimal(0)
    with Pool(8) as p:
        result = p.map(calc, range(0, DIGITS, 1))
        # print(result)
        pi = Decimal(1) / (Decimal(12) * sum(result))
    end = time() - start

    print(f'PI = {pi}')
    print(f'TIME = {end}')