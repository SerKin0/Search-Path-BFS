"""
    '0' - координата в которой еще не была программа
    's' - старт
    'f' - финиш
    '#' - стены
    '1', '2', ... - шаги
"""

map_mass = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '#', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
]

step = 1
x_len, y_len = 10, 10       # Размеры поля
start_x, start_y = 1, 1     # Координаты Стартовой точки
finish_x, finish_y = 9, 9   # Координаты Финишной точки
flag = False                # Достигли мы финиша?
map_mass[start_y][start_x] = '1'

# mass[y][x]
def move(x: int, y: int):
    global x_len, y_len, map_mass, flag
    if (0 <= x <= x_len) and (0 <= y <= y_len):
        tmp = [False, False, False, False]  # Вверх, вправо, вниз, влево
        # Up +
        if (y - 1 >= 0) and (map_mass[y - 1][x] == '0'):
            tmp[0] = True
        else:
            if map_mass[y - 1][x] == 'f':
                flag = True
                return None
            else:
                tmp[0] = False
        # Right +
        if (x + 1 <= x_len - 1) and (map_mass[y][x + 1] == '0'):
            tmp[1] = True
        else:
            if map_mass[y][x + 1] == 'f':
                flag = True
                return None
            else:
                tmp[1] = False
        # Down +
        if (y + 1 <= y_len - 1) and (map_mass[y + 1][x] == '0'):
            tmp[2] = True
        else:
            if map_mass[y + 1][x] == 'f':
                flag = True
                return None
            else:
                tmp[2] = False
        # Left +
        if (x - 1 >= 0) and (map_mass[y][x - 1] == '0'):
            tmp[3] = True
        else:
            if map_mass[y][x - 1] == 'f':
                flag = True
                return None
            else:
                tmp[3] = False
        return tmp
    else:
        return None


def pos(x: int, y: int, sec_st: str):
    tmp = move(x, y)
    if tmp[0]:
        map_mass[y - 1][x] = sec_st
    if tmp[1]:
        map_mass[y][x + 1] = sec_st
    if tmp[2]:
        map_mass[y + 1][x] = sec_st
    if tmp[3]:
        map_mass[y][x - 1] = sec_st


def printMap():
    for i in map_mass:
        print(*i)


while not flag:
    tmp_st = str(step)
    for y in range(y_len):
        for x in range(x_len):
            if map_mass[y][x] == tmp_st:
                print(x, y)
                pos(x, y, str(step + 1))
    step += 1

printMap()