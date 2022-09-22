from protected_input import protected_input


def square_triangle(a, b, c):
    p = (a + b + c) / 2  # Формула Герона
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def start():
    m_num = [None] * 3
    m_sqr = [None] * 2
    print('Задача: сравнение площадей')
    for j in range(2):
        for i in range(3):
            while True:
                print('Введите %d сторону для %d треугольника' % ((i + 1), (j + 1)))
                num = protected_input(True)
                if num > 0:
                    m_num[i] = num
                    break
                else:
                    print('Сторона не может быть отрицательной')
        m_sqr[j] = square_triangle(m_num[0], m_num[1], m_num[2])
    if m_sqr[0] == m_sqr[1]:
        print('Площади треугольников равны')
    else:
        print('Площади треугольников не равны')
