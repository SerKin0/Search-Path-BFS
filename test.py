import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time


im = Image.open('1.png')
na = np.array(im).tolist()
na = [list(map(lambda t: '0' if 255*2 <= t[0] + t[1] + t[2] <= 255 * 3 else "#", i)) for i in na]
x_len, y_len = im.size  # Размеры поля
map_mass = na

step = 1  # Шаг
start_x, start_y = 1, 1  # Координаты Стартовой точки
finish_x, finish_y = x_len-1, y_len-1  # Координаты Финишной точки

flag = False  # Достигли мы финиша?

map_mass[start_y][start_x] = '1'  # Устанавливаем единицу в точку старта
map_mass[finish_y][finish_x] = 'f'  # Устанавливаем символ f в точку финиша


# Функция возвращает массив с вариантом доступных передвижений в стороны
# (Up, Right, Down, Left) - Если можно передвинутся, то True, если нет, то False
def move(move_x: int, move_y: int):
    global x_len, y_len, map_mass, flag, moving
    # Если координаты находятся в размерах массива, то
    if (0 <= move_x <= x_len) and (0 <= move_y <= y_len):
        var = [False, False, False, False]  # Вверх, вправо, вниз, влево
        # Up
        if move_y - 1 >= 0:
            if map_mass[move_y - 1][move_x] == 'f':  # Если при движении в эту сторону мы можем достать до финиша, то...
                flag = True  # ...Прекращаем перебор
            elif map_mass[move_y - 1][move_x] == '0':  # Если же, там 0, то...
                var[0] = True  # ...значит туда можно передвигаться
        # Right
        if move_x + 1 <= x_len - 1:
            if map_mass[move_y][move_x + 1] == 'f':
                flag = True
            elif map_mass[move_y][move_x + 1] == '0':
                var[1] = True
        # Down
        if move_y + 1 <= y_len - 1:
            if map_mass[move_y + 1][move_x] == 'f':
                flag = True
            elif map_mass[move_y + 1][move_x] == '0':
                var[2] = True
        # Left
        if move_x - 1 >= 0:
            if map_mass[move_y][move_x - 1] == 'f':
                flag = True
            elif map_mass[move_y][move_x - 1] == '0':
                var[3] = True
        return var
    # Иначе, возвращаем None
    else:
        return None


# Расставляет следующие значения в разные стороны
def pos(mass, pos_x: int, pos_y: int, sec_st: str, var):
    if var[0]:
        mass[pos_y - 1][pos_x] = sec_st
    if var[1]:
        mass[pos_y][pos_x + 1] = sec_st
    if var[2]:
        mass[pos_y + 1][pos_x] = sec_st
    if var[3]:
        mass[pos_y][pos_x - 1] = sec_st


# Вывод карты с вариантами
def printMap(mass, title=None):
    if title:
        print(title)
    for i in mass:
        for j in i:
            print(j, end='\t')
        print()
    print()


start = time.time()
# Пока мы не сможем достичь финиша,...
while not flag:
    moving = False
    tmp_st = str(step)
    for y in range(y_len):
        for x in range(x_len):
            if map_mass[y][x] == tmp_st:
                tmp = move(x, y)
                print(tmp)
                if tmp[0] or tmp[1] or tmp[2] or tmp[3]:
                    pos(x, y, str(step + 1), tmp)
                    moving = moving or True
                else:
                    moving = moving or False
    printMap(map_mass)
    if not moving:
        print("Движение не возможно!")
        break
    # printMap(map_mass)
    step += 1

# printMap(map_mass, "Массив шагами до финиша:")
print(f"Count step = {step}\nTime = {time.time() - start}")

int_map_mass = [list(map(lambda t: -1 if t == 'f' or t == "#" else int(t), i)) for i in map_mass]
fig, ax = plt.subplots()
x, y = finish_x, finish_y
wall = -100
while step != 1:


# printMap(int_map_mass, "Массив с путем на финиш:")
ax.imshow(int_map_mass)
plt.show()
