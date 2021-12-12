import threading
import multiprocessing
from time import time
import sys

vector1 = []
vector2 = []

def progress_bar(current, total, barLength=50):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rMultiplying: [%s%s]' % (arrow, spaces))

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

for i in range(100):
    vector1.append(i)
    vector2.append(i+1)

def multiplyVectors(index):
    vector1[index] = vector1[index] * vector2[index] + factorial(100000)

start = time()

if __name__ == '__main__':
    multiprocessing.freeze_support() 

    for i in range(len(vector2)):
        # multiplyVectors(i)
        thread = multiprocessing.Process(target=multiplyVectors, args=(i, ))
        thread.start()
        progress_bar(i, len(vector2), 50)

    timeStop = time() - start
    print(f'VECTOR = {vector1}')
    print(f'TIME = {timeStop}')