from protected_input import protected_input


def square_triangle(a, b):
    return b * (a ** 2 - b ** 2 / 4) ** 0.5 / 2


def start():
    print('Задача: вычисление площади равнобедренного треугольника')
    m_a_b = [None, None]
    for i in range(2):
        while True:
            print('Введите %d сторону' % (i + 1))
            num = protected_input(True)
            if num > 0:
                m_a_b[i] = num
                break
            else:
                print('Сторона не может быть отрицательной')
    if m_a_b[0] * 2 > m_a_b[1]:
        sqr = square_triangle(m_a_b[0], m_a_b[1])
        if float(sqr) % 2.0 == 0.0:
            print('Полуплощадь равна %d' % int(sqr / 2))
        else:
            print('Площадь равна %10.2f' % sqr)
    else:
        print('Не соблдюдается правило: сумма двух сторон больше третьей')
