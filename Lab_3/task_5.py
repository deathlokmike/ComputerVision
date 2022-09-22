from PIL import Image
from graph import save_hist
from numpy import histogram, interp, array


def align_hist(image, step=256):
    arr_image = array(image)
    imh, b = histogram(arr_image.flatten(), step, normed=True)
    cdf = imh.cumsum()
    cdf = 255 * cdf / cdf[-1]
    res = interp(arr_image.flatten(), b[:-1], cdf)
    return res.reshape(arr_image.shape)


def start():
    print('Задача: выровнять гистограмму')
    grayscale = Image.open('P1.jpg').convert('L')  # преобразование в полутона
    align = align_hist(grayscale)  # выравнивание гистограммы
    m_result = [['Полутоновое', grayscale], ['Выровненное', align]]
    save_hist(m_result, num_task=5)



