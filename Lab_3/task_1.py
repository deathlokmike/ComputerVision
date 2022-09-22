from PIL import Image


def start():
    print('Задача: определить размер картинки Р1')
    try:
        im = Image.open('P1.jpg')
        buf = im.size
        print('Размер картинки:\nШирина: %d px\nВысота: %d px' % (buf[0], buf[1]))
    except FileNotFoundError:
        print('Положите картинку P1.txt  в корневую папку')
