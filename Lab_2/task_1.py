import matplotlib.pyplot as plt
import numpy as np

# GLOBAL VAL
x = np.arange(-5, 5, 0.1)
y1 = 2 * x + 3
y2 = 4 * x ** 2 - 4
y3 = np.exp(-x)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')


def three_in_one():
    plt.plot(x, y1, '--r', label='y=2x+3')
    plt.plot(x, y2, 'b', label='y=2x+3')
    plt.plot(x, y3, '*-y', label='y=e^x')
    plt.legend()
    plt.gca().set_facecolor('k')
    plt.show()


def three_in_three():
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, 'r')
    plt.grid()
    plt.title('y=2x+3', fontsize=10)
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, 'b')
    plt.grid()
    plt.title('y=2x+3', fontsize=10)
    plt.subplot(2, 2, 3)
    plt.plot(x, y3, 'k')
    plt.grid()
    plt.title('y=e^x', fontsize=10)
    plt.show()


three_in_one()
three_in_three()
