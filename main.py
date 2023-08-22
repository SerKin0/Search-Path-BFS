import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from BFS import printMap, bfs_alg


def f(t: tuple):
    red, green, blue, x = t
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
x = bfs_alg(map_mass)
printMap(x)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax.imshow(x)
plt.show()
