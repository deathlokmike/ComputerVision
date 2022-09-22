from protected_input import protected_input


def start():
    m_num = []
    m_buf = []
    print('Задача: произвольные числа в указанных границах')
    for i in range(3):
        print('Введите %d число ' % (i + 1))
        m_buf.append(protected_input(True))
    for num in m_buf:
        if 1 <= num <= 3:
            m_num.append(num)
    if len(m_num) > 0:
        buf_str = 'Числа, лежащие в границах [1; 3]:'
        for num in m_num:
            buf_str += ' ' + str(num) + ','
        print(buf_str)
    else:
        print('Чисел, лежащих в границах [1; 3] - нет')
