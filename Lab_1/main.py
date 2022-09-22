from protected_input import protected_input
import task_2
import task_5
import task_7
import task_8
import task_9
import task_13


if __name__ == '__main__':
    while True:
        print('Выберите задание\nЗадача 1.\nЗадача 2.\nЗадача 3.\nЗадача 4.\nЗадача 5.\nЗадача 6.\n7. Выход.\n')
        menu_i = protected_input(False)
        if menu_i == 1:
            task_2.start()
        elif menu_i == 2:
            task_5.start()
        elif menu_i == 3:
            task_7.start()
        elif menu_i == 4:
            task_8.start()
        elif menu_i == 5:
            task_9.start()
        elif menu_i == 6:
            task_13.start()
        elif menu_i == 7:
            break
        else:
            print('Ошибка в меню')
