from turtle import *


def draw():  # логотип группы BMTH
    color('black')
    bgcolor('orange')
    ht()
    width(3)
    speed(100)
    setpos(-145, 75)
    setpos(-40, -20)
    setpos(0, -175)
    setpos(40, -20)
    setpos(145, 75)
    setpos(-145, -75)
    setpos(-40, 20)
    setpos(0, 175)
    setpos(40, 20)
    setpos(145, -75)
    setpos(0, 0)
    up()
    setpos(0, -190)
    down()
    circle(190)
    up()
    setpos(190, -250)
    write('Дроздов М. А. АА-18-05', font=("Arial", 16, "normal"))
    done()


draw()
