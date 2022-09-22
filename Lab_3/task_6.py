from PIL import Image
from graph import save_hist
from skimage import util
from numpy import array, uint8


def start():
    print('Задача: наложить шум')
    grayscale = Image.open('P1.jpg').convert('L')  # преобразование в полутона
    noise = util.random_noise(array(grayscale), mode='salt')  # наложение шума
    # pepper - черный шум
    Image.fromarray(uint8(255 * noise)).save('P6.png')
    m_result = [['Полутоновое', grayscale], ['Шумное', noise]]
    save_hist(m_result, num_task=6)
