import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from BFS import printMap, bfs_alg, return_bfs


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


im = Image.open('1.png')
mass = np.array(im).tolist()
x_len, y_len = im.size  # Размеры поля
map_mass = [list(map(lambda t: f(t), i)) for i in mass]

# Создание данных для первого графика
data1 = bfs_alg(map_mass)
printMap(data1)

# Создание данных для второго графика
data2 = return_bfs(data1)
printMap(data2)

# Создание сетки графиков
fig, (ax1, ax2) = plt.subplots(1, 2)

# Первый график imshow
im1 = ax1.imshow(data1)
ax1.set_title('График 1')

# Второй график imshow
im2 = ax2.imshow(data2)
ax2.set_title('График 2')

# Цветовая шкала для второго графика
plt.colorbar(im2, ax=[ax1, ax2])

# Отображение графиков
plt.show()
