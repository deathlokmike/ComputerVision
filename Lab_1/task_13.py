from math import sin


def my_func():
    x = 1.625
    y = -15.4
    z = 0.252
    a = (abs(y) ** (x + 1)) / ((abs(x - 2) + 3) ** (1 / 3)) + (x + y / 2) / (2 * abs(x + y))
    b = (x + 1) ** (-1 / sin(z))
    return [a, b]


def start():
    mass = my_func()
    print('Подсчет функции:\na = %5.4f, b = %5.4f' % (mass[0], mass[1]))
