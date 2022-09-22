from PIL import Image, ImageOps, ImageEnhance
from graph import save_hist


def start():
    print('Задача: построить гистограммы для полутонового и инвертированного изображения')
    grayscale = Image.open('P1.jpg').convert('L')  # преобразование в полутона
    inverted = ImageOps.invert(grayscale)  # инвертируем изображение
    bright = ImageEnhance.Brightness(grayscale).enhance(2)  # увеличим яркость изображения
    m_result = [['Полутоновое', grayscale], ['Инвертированное', inverted], ['Яркое', bright]]
    save_hist(m_result, num_task=4)



