from threading import Thread
import sys
from decimal import *
from math import factorial
from time import time

def progress_bar(current, total, barLength=50):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rFinding PI: [%s%s]' % (arrow, spaces))

# def getPI(n):
#     k = 0
#     pi = Decimal(0)
#     while k < n:
#         threadPI = []
#         thread = Thread(target=lambda x:  threadPI.append(chudnovsky(x)), args=(k,))
#         thread.start()
#         progress_bar(k, n, 75)  
#         if threadPI != []:
#             pi += threadPI[0]
#         k += 1
#     pi = pi * Decimal(10005).sqrt()/4270934400
#     pi = pi**(-1)
#     return pi

class BaseThread(Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self):
        self.method()
        if self.callback is not None:
            self.callback(*self.callback_args)

pi = Decimal(0)
k = 0
# def callback(threadPI):
#     global k
#     global pi
    
#     pi += threadPI
#     k += 1

def chudnovsky(localK):
    global pi
    global k
    pi += (Decimal(-1)**localK)*(Decimal(factorial(6*localK))/((factorial(localK)**3)*(factorial(3*localK)))* (13591409+545140134*localK)/(640320**(3*localK)))
    k += 1


def getPI(n):
    global k
    global pi
    
    while k < n:
        if k / 2 != 0:
            thread1 = Thread(target=chudnovsky, args=(k,))
            thread1.start()
            thread1.join()
        else:
            thread2 = Thread(target=chudnovsky, args=(k,))
            thread2.start()
            thread2.join()

        # progress_bar(k, n, 75)

        # if threadPI != []:
        #     pi += threadPI[0]
        # k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


DIGITS = 1000  # <--- Знаки после запятой
start = time()

endpi = getPI(DIGITS)

time_stop = time()-start

print (f"\nPi = %.{DIGITS}f" % (pi))
# print (f"\nPi = " , endpi)
# print (f"\nPi = ", "{0:10e}".format(pi))
print (f"Time: {time_stop}")
print (f"Max numbers: {DIGITS}")
