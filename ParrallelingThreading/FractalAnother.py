from PIL import Image
import time

class TimeCounter:

    # конструктор
    def __init__(self):
        print('Object initialized')
        self.start = time.process_time()
    # деструктор
    def __del__(self):
        print('Object destroyed')
        self.elapsed_time = time.process_time() - self.start
        print('Время выполнения (сек): ', self.elapsed_time)


# настройка ширины, высоты и масштабирования
# изображения, которое будет создано
obj = TimeCounter()

w, h, zoom = 1920,1080,1
# создание нового изображения в режиме RGB

bitmap = Image.new("RGB", (w, h), "white")

pix = bitmap.load()
# установка переменных в соответствии с
# уравнение для создания фрактала

cX, cY = -0.7, 0.34
moveX, moveY = 0.0, 0.0
maxIter = 20

for x in range(w):
    for y in range(h):
        zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
        zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
        i = maxIter
        while zx*zx + zy*zy < 4 and i > 1:
            tmp = zx*zx - zy*zy + cX
            zy,zx = 2.0*zx*zy + cY, tmp
            i += 1
            # конвертировать байт в RGB (3 байта)
            pix[x,y] = (i << 21) + (i << 10) + i*8
# для отображения созданного фрактала
bitmap.show()