from protected_input import protected_input


def start():
    print('Задача: перевести число из СИ в кг')
    m_weigh = [1, 10 ** 6, 10 ** -3, 10 ** 3, 10 ** 2]
    while True:
        print('Выберите СИ:\n1. Кг\n2. мг\n3. г\n4. т\n5. цн\n Или напишите exit')
        SC = protected_input(False)
        if type(SC) is bool:
            return
        else:
            if 1 <= SC <= 5:
                print('Введите массу:')
                weight = protected_input(True)
                if weight > 0:
                    print('Масса: ' + str(weight * m_weigh[SC - 1]) + ' кг')
                else:
                    print('Отрицательная масса')
            else:
                print('Неверное число')
