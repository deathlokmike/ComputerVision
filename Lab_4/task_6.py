import matplotlib.pyplot as plt
from skimage import io, filters, measure
from scipy import ndimage


def count_objects(image, i):
    im = io.imread(image, as_gray=True)
    # пороговое значение
    val = filters.threshold_otsu(im)
    # бинарное преобразование
    drops = ndimage.binary_fill_holes(im < val)
    # поиск объектов
    labels = measure.label(drops)
    plt.imshow(drops, cmap='gray')
    plt.axis('off')
    plt.title(f'Количество объектов: {labels.max()}')
    plt.savefig(f'result_task_6_{i}.png')
    plt.show()


def start():
    m_image = ['dots.jpeg', 'eyes.png', 'panda.jpg']
    for i, image in enumerate(m_image):
        count_objects(image, i + 1)
