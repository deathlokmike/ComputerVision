from protected_input import protected_input


def start():
    print('Задача: определить високосный год')
    while True:
        print('Напишите год или exit\n')
        year = protected_input(False)
        if type(year) is bool:
            return
        else:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                print('Високосный')
            else:
                print('Невисокосный')
