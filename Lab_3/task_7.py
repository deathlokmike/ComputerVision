from PIL import Image
from graph import save_hist, save_isolines
from skimage.filters import gaussian
from numpy import array


def start():
    print('Задача: выполнить размытие по Гауссу')
    grayscale = Image.open('P1.jpg').convert('L')  # преобразование в полутона
    m_sigma = [15, 30, 80]
    m_result = [['Полутоновое', grayscale]]
    for custom_sigma in m_sigma:
        m_result.append(['Сигма = %d' % custom_sigma, gaussian(array(grayscale), sigma=custom_sigma)])
    save_hist(m_result, num_task=7)
    save_isolines(m_result)
