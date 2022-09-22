from protected_input import protected_input


def expression(x, y, z):
    return (((x ** 5 + 7) / (6 * y)) ** (1 / 3)) / (7 - z % y)


def start():
    m_num = []
    m_str = ['x', 'y', 'z']
    print('Задача: вычисление выражения')
    for i in range(3):
        print('Введите %s' % m_str[i])
        m_num.append(protected_input(True))
    print('Результат: ' + str(expression(m_num[0], m_num[1], m_num[2]))
          + ' (вывод не форматирован, тк результат может оказаться комплексным')
    # вывод не форматирован, т.к. результат может оказаться комплексным


