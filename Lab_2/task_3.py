from random import randrange
from tkinter import *
from PIL import Image, ImageTk

# глобальная переменная для сигнало о продолжение движения фото
GLOBAL_STATE = True


def right_click(photo):
    global GLOBAL_STATE
    if GLOBAL_STATE:
        GLOBAL_STATE = False
    else:
        GLOBAL_STATE = True
        photo.movement()  # повторный запуск движения


class movablePhoto:
    def __init__(self, cvs):
        self._cvs = cvs
        self.pht = self._cvs.create_image(0, 0, anchor='nw', image=img)
        self.movement()

    def move(self, x, y):
        self._cvs.moveto(self.pht, x, y)  # переместить фото в точку, где находится курсор мыши

    def movement(self):
        x = randrange(-4, 4, 1)  # рандомные передвижения для х и у
        y = randrange(-4, 4, 1)
        self._cvs.move(self.pht, x, y)
        if GLOBAL_STATE:
            self._cvs.after(30, self.movement)  # рекурсия функции движения


if __name__ == '__main__':
    window = Tk()
    window.title('Задание 3. Нажимайте правую и левую кнопку мыши')
    window.geometry('1280x720')
    canvas = Canvas(window, width=1920, heigh=1080)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open('1.jpg'))
    pht = movablePhoto(canvas)  # объект-фото
    window.bind('<Button-1>', lambda event: pht.move(event.x, event.y))  # бинд левой кнопки
    window.bind('<Button-3>', lambda event: right_click(pht))  # бинд правой конпки
    window.mainloop()
