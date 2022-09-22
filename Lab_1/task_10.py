from protected_input import protected_input


def start():
    m_num = []
    m_buf = []
    print('Задача: минимальное из положительных')
    for i in range(3):
        print('Введите %d число ' % (i + 1))
        m_buf.append(protected_input(True))
    for num in m_buf:
        if num > 0:
            m_num.append(num)
    if len(m_num) > 0:
        print(('Положительных чисел: %d, минимальное: ' + str(min(m_num))) % len(m_num))
    else:
        print('Положительных чисел нет')
