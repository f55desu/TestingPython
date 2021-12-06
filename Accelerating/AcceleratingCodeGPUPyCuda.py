from matplotlib import pyplot as plt
from pylab import imshow, show
import numpy as np
from timeit import default_timer as timer
import sys

def progress_bar(current, total, barLength=50):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rСоздаётся фрактал: [%s%s]' % (arrow, spaces))

def mandel(x, y, max_iters):

    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iters