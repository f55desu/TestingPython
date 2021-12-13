import threading
from time import time
import sys

vector1 = []
vector2 = []
vector3 = []

def progress_bar(current, total, barLength=50):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rMultiplying vectors: [%s%s]' % (arrow, spaces))

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

for i in range(10):
    vector1.append(i)
    vector2.append(i+1)

def multiplyVectors(index):
    global vector1
    vector1[index] = vector1[index] * vector2[index] + factorial(100000)

start = time()

for i in range(len(vector2)):
    progress_bar(i, len(vector2), 50)
    # multiplyVectors(i)        #   1 Main Thread, fact(100000) = 68,1 sec
    thread = threading.Thread(target=multiplyVectors, args=(i, )) # 10 Threads, fact(100000) = 10,6 sec
    thread.start()

timeStop = time() - start
print(f'\nVECTOR = {vector1}')
print(f'TIME = {timeStop}')