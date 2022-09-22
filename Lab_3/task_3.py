from PIL import Image, ImageDraw, ImageColor


def start(grad=120):
    print('Задача: Повернуть область изображения')
    im = Image.open('P1.jpg')
    crop_cord = [100, 300, 400, 620]  # Координаты обрезки
    draw = ImageDraw.Draw(im)  # Создание обводки вокруг изображения
    cords = [(crop_cord[0], crop_cord[1]), (crop_cord[2], crop_cord[1]), (crop_cord[2], crop_cord[3]),
             (crop_cord[0], crop_cord[3]), (crop_cord[0], crop_cord[1])]
    red = ImageColor.getrgb('red')
    draw.line(cords, fill=red, width=5)
    sub_image = im.crop(box=(crop_cord[0], crop_cord[1], crop_cord[2], crop_cord[3])).rotate(grad)
    im.paste(sub_image, box=(crop_cord[0], crop_cord[1]))
    im.save('P3.jpg')

