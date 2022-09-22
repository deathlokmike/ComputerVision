from PIL import Image, ImageOps, ImageEnhance
from scipy.ndimage.filters import sobel, gaussian_filter
import matplotlib.pyplot as plt
from numpy import array, zeros, sqrt


def save_hist(mass: list, num_subtask: int):
    plt.subplots_adjust(wspace=0.3, hspace=0)
    plt.gray()
    for i, data in enumerate(mass):
        if i == 0:
            plt.subplot(2, 2, i + 1), plt.hist(data.flatten(), 128)
        else:
            plt.subplot(2, 2, i + 1), plt.imshow(data)
    plt.show()
    plt.savefig(f'task_4_{num_subtask}_result.png')
    plt.close()


def start():
    print('Задача: Определить границы с использованием операторов Собеля и Гаусса')
    sigma = 5  # значение размытия
    m_im = array(Image.open('P1.jpg').convert('L'))
    # пустые массивы для значений производной
    m_imx = zeros(m_im.shape)
    m_imy = zeros(m_im.shape)
    # Производная по х
    sobel(m_im, 1, m_imx)
    # Производная по у
    sobel(m_im, 0, m_imy)
    # Величина градиента
    m = sqrt(m_imx**2 + m_imy**2)
    # сохранение
    save_hist([m, m_imx, m_imy, m], 1)
    gaussian_filter(m_im, (sigma, sigma), (0, 1), m_imx)
    gaussian_filter(m_im, (sigma, sigma), (1, 0), m_imy)
    m = sqrt(m_imx ** 2 + m_imy ** 2)
    save_hist([m, m_imx, m_imy, m], 1)

