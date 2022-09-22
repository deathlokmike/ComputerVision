from protected_input import protected_input


def arithmetic_mean(mass):
    return sum(mass) / len(mass)


def geometric_mean(mass):
    buf = 1
    for x in mass:
        buf *= x
    return buf ** (1 / len(mass))


def same_sign(a, b):
    if a * b > 0:
        return True
    else:
        return False


def task_11():
    m_num = []
    print('Задача: вычисление арифмитического и геометрического')
    for i in range(2):
        print('Введите %d число ' % (i + 1))
        m_num.append(protected_input(True))
    if same_sign(m_num[0], m_num[1]):
        print('Среднее геометрическое: ' + str(geometric_mean(m_num)))
    else:
        print('Среднее арифмитическое: ' + str(arithmetic_mean(m_num)))
