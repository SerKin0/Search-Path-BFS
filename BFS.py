import time


# Функция возвращает массив с вариантом доступных передвижений в стороны
# (Up, Right, Down, Left) - Если можно передвинутся, то True, если нет, то False
def move(mass: list, move_x: int, move_y: int, x_len: int, y_len: int):
    flag = False
    # Если координаты находятся в размерах массива, то
    if (0 <= move_x <= x_len) and (0 <= move_y <= y_len):
        var = [False, False, False, False]  # Вверх, вправо, вниз, влево
        # Up
        if move_y - 1 >= 0:
            if mass[move_y - 1][move_x] == -2:  # Если при движении в эту сторону мы можем достать до финиша, то...
                flag = True  # ...Прекращаем перебор
            elif mass[move_y - 1][move_x] == 0:  # Если же, там 0, то...
                var[0] = True  # ...значит туда можно передвигаться
        # Right
        if move_x + 1 <= x_len - 1:
            if mass[move_y][move_x + 1] == -2:
                flag = True
            elif mass[move_y][move_x + 1] == 0:
                var[1] = True
        # Down
        if move_y + 1 <= y_len - 1:
            if mass[move_y + 1][move_x] == -2:
                flag = True
            elif mass[move_y + 1][move_x] == 0:
                var[2] = True
        # Left
        if move_x - 1 >= 0:
            if mass[move_y][move_x - 1] == -2:
                flag = True
            elif mass[move_y][move_x - 1] == 0:
                var[3] = True
        return var, flag
    # Иначе, возвращаем None
    else:
        return None


# Расставляет следующие значения в разные стороны
def pos(mass, pos_x: int, pos_y: int, sec_st: int, var):
    if var[0]:
        mass[pos_y - 1][pos_x] = sec_st
    if var[1]:
        mass[pos_y][pos_x + 1] = sec_st
    if var[2]:
        mass[pos_y + 1][pos_x] = sec_st
    if var[3]:
        mass[pos_y][pos_x - 1] = sec_st


# Вывод карты с вариантами
def printMap(mass: list, title=None):
    if title:
        print(title)
    for i in mass:
        for j in i:
            print(j, end='\t')
        print()
    print()


"""
    Выводит массив с расставленными значениями пути
     0 - пустые места
     1 - старт
    -1 - стена
    -2 - финиш
"""


def bfs_alg(map_mass: list):
    flag = False
    start = time.time()
    step = 1  # Шаг
    x_len, y_len = len(map_mass[0]), len(map_mass)
    while not flag:
        moving = False
        for y in range(y_len - 1):
            for x in range(x_len - 1):
                if map_mass[y][x] == step:
                    tmp, flag = move(map_mass, x, y, x_len, y_len)
                    if tmp[0] or tmp[1] or tmp[2] or tmp[3]:
                        pos(map_mass, x, y, step + 1, tmp)
                        moving = moving or True
                    else:
                        moving = moving or False
        if not moving and not flag:
            print("Движение не возможно!")
            return map_mass
        step += 1
    print(f"Count step = {step}\nTime = {time.time() - start}")
    return map_mass
