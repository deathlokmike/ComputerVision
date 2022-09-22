from PIL import Image


def start():
    print('Задача: сделать цветную и ЧБ миниатюру')
    im = Image.open('P1.jpg')
    im.thumbnail((240, 180))  # создание миниатюры
    im.save('P2.jpg')
    im = im.convert('1')  # преобразование в ЧБ
    im.save('P2_BW.jpg')
