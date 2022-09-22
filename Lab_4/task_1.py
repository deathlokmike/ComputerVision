from PIL import Image
from random import randrange


def start():
    print('Задача: Наложить одно фото на другое по центру и в произвольной области')
    try:
        original = Image.open('P1.jpg')
        image_overlay = Image.open('emoji.png')
        copy = original.copy()
        # размеры изображений
        original_size = original.size
        overlay_size = image_overlay.size
        # высчитываем координаты центра
        cords_center = ((original_size[0] - overlay_size[0])//2, (original_size[1] - overlay_size[1])//2)
        # высчитываем рандомные координаты
        cords_rand = (randrange(0, original_size[0], 1),
                      randrange(0, original_size[1], 1))
        # накладываем изображения
        original.paste(image_overlay, cords_center)
        copy.paste(image_overlay, cords_rand)
        # сохраняем изображения
        original.save('result_task_1_1.jpg')
        copy.save('result_task_1_2.jpg')
        print('Изображения сохранены')
    except FileNotFoundError:
        print('Положите картинку P1.txt  в корневую папку')
