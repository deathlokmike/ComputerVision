import task_1
import task_2
import task_3
import task_4
import task_5
import task_6
import task_7
from protected_input import protected_input


def main():
    while True:
        print('Выберите задание\nЗадача 1.\nЗадача 2.\nЗадача 3.\nЗадача 4.\n'
              'Задача 5.\nЗадача 6.\nЗадача 7.\n8. Выход.\n')
        i = protected_input(False)
        if i == 1:
            task_1.start()
        elif i == 2:
            task_2.start()
        elif i == 3:
            task_3.start(-90)
        elif i == 4:
            task_4.start()
        elif i == 5:
            task_5.start()
        elif i == 6:
            task_6.start()
        elif i == 7:
            task_7.start()
        elif i == 8:
            return
        else:
            print('Ошибка в меню')


if __name__ == '__main__':
    main()
