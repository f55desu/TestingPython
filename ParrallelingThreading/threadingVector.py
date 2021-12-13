from multiprocessing import *
from time import time
from concurrent.futures import ThreadPoolExecutor

vector1 = []
vector2 = []

for i in range(10000000):
    vector1.append(i)
    vector2.append(i+1)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def calc(index):
    return vector1[index] + vector2[index]

if __name__ == '__main__':

    start = time()
    with ThreadPoolExecutor(maxworkers=8) as executor:
        print(executor.map(calc, range(0, len(vector1), 1)))
    end = time() - start
    print(f'TIME = {end}')