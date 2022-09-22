import matplotlib.pyplot as plt
from numpy import array


def save_hist(mass: list, num_task: int):
    plt.subplots_adjust(wspace=0.1, hspace=0.5)
    plt.gray()
    count_row = len(mass)
    for i in range(1, len(mass) * 2 + 1, 2):
        j = (i - 1) // 2
        plt.subplot(count_row, 2, i), plt.hist(array(mass[j][1]).flatten(), 256)
        plt.subplot(count_row, 2, i + 1), plt.imshow(array(mass[j][1]))
        plt.axis('off')
        plt.title(mass[j][0], fontsize=10)

    plt.savefig('task_%d_result.png' % num_task)
    plt.close()


def save_isolines(mass: list):
    for result in mass:
        plt.contour(result[1], origin="image")  # рисование изолиний
        plt.axis("equal")
        plt.axis("off")
        plt.savefig('Изолинии %s' % result[0].lower())
        plt.figure()
