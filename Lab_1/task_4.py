from protected_input import protected_input
from math import cos, sin


def task_4():
    m_num = []
    print('Задача: определние синуса и косинуса')
    for i in range(4):
        print('Введите число %d:' % (i + 1))
        m_num.append(protected_input(True))
    num = min(m_num)
    print('Минимальное число %10.2f. Косинус этого числа %10.2f. Синус этого числа %10.2f.'
          % (num, cos(num), sin(num)))
    num = max(m_num)
    print('Максимальное число %10.2f. Косинус этого числа %10.2f. Синус этого числа %10.2f.'
          % (num, cos(num), sin(num)))
