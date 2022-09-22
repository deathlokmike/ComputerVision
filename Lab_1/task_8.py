from protected_input import protected_input


def start():
    m_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
    print('Задача: определение месяца')
    while True:
        print('Напишите число (1-12) или exit\n')
        number = protected_input(False)
        if type(number) is bool:
            return
        else:
            if 1 <= number <= 12:
                print('Месяц: %s' % m_month[number - 1])
            else:
                print('Число не в диапазоне')
