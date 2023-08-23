import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from BFS import bfs_alg, return_bfs


def f(t: tuple):
    red, green, blue, _ = t
    if red == 255 and green == 0 and blue == 0:
        return 1
    elif red == 255 and green == 255 and blue == 255:
        return 0
    elif red == 0 and green == 0 and blue == 0:
        return -1
    elif red == 0 and green == 0 and blue == 255:
        return -2


im = Image.open('image.png')
image_mass = np.array(im).tolist()
x_len, y_len = im.size  # Размеры поля
map_mass = [list(map(lambda t: f(t), i)) for i in image_mass]

# Создание данных для первого графика
data1 = bfs_alg(map_mass)

# Создание первого графика
plt.figure()
plt.imshow(data1)
plt.title('Градиент к финишу')

# Создание данных для второго графика
data2 = return_bfs(data1)

# Создание второго графика
plt.figure()
plt.imshow(data2)
plt.title('Путь к финишу')

# Отображение графиков
plt.show()
