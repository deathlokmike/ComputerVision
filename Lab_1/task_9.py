from protected_input import protected_input
from math import pi


def rad_to_grad(val):
    return val * 180 / pi


def grad_to_rad(val):
    return val * pi / 180


def start():
    print('Задача: перевод из радиан в градусы и обратно')
    while True:
        print('1. Из градусов в радианы\n2. Из радиан в градусы\nЧтобы выйти, напишите exit')
        menu = protected_input(False)
        if type(menu) is bool:
            return
        else:
            print('Напишите число:')
            num = protected_input(True)
            if menu == 1:
                print('Ответ: %3.4f' % grad_to_rad(num))
            elif menu == 2:
                print('Ответ: %3.4f' % rad_to_grad(num))
            else:
                print('Неверное число')
