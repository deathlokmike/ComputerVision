from PIL import Image


def start():
    print('Создать маску и применить ее к изображению')
    source = Image.open('P1.jpg')
    res_img = Image.open('emoji.png')
    mask_im = Image.open('mask.png').resize(res_img.size).convert('L')
    source.paste(res_img, (300, 10), mask_im)
    source.save('result_task_2.jpg')
    print('Результат сохранен в result_task_2.jpg')
