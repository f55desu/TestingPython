from numba import jit, njit, vectorize
from matplotlib import pyplot as plt
from pylab import imshow, show
import numpy as np
from timeit import default_timer as timer
from concurrent.futures import ThreadPoolExecutor
import sys

def progress_bar(current, total, barLength=50):
    progress = float(current) * 100 / total
    arrow = '#' * int(progress / 100 * barLength - 1)
    spaces = ' ' * (barLength - len(arrow))
    sys.stdout.write('\rСоздаётся фрактал: [%s%s]' % (arrow, spaces))

@jit
def mandel(x, y, max_iters):

    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    
    return max_iters
@jit(nogil=True)
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            img = min_y + y * pixel_size_y
            color = mandel(real, img, iters)
            image[y, x] = color
        progress_bar(x, width, 75)

user_iters = int(input("Введите количество итераций фрактала: "))
image = np.zeros((1024, 1536), dtype = np.uint8)
start = timer()
with ThreadPoolExecutor(8) as ex:
    ex.map(create_fractal(-2.0, 1.0, -1.0, 1.0, image, user_iters))
seconds = timer() - start

print('\nСоздан фрактал за %f секунд' % seconds)
imshow(image)
show()