# Первый урок программирования на Phyton

import turtle
window = turtle.Screen()
t = turtle.Pen()

#t.reset()
t.forward(50)
#t.up()
t.left(90)
t.forward(50)
#t.down()
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
#input("Press any key to exit ...")

from random import random


jakob = turtle.Pen()

for i in range(5):
    steps = int(random() * 100)
    angle = int(random() * 360)
    jakob.right(angle)
    jakob.fd(steps)






tur=turtle.Pen()
tur.forward(100)
tur2=turtle.Pen()
tur2.left(90)
tur2.forward(100)
tur2.right(90)
tur2.forward(100)



#t.reset()
#for x in range(1, 9):
#    t.forward(100)
#    t.left(225)

#t.screen.mainloop()

#t.reset()
#for x in range(1, 38):
#    t.forward(300)
#    t.left(175)

#t.reset()
#for x in range(1, 20):
#    t.forward(300)
#    t.left(95)

#t.reset()
#for x in range(1, 19):
#    t.forward(100)
#    if x % 2 == 0:
#        t.left(175)
#    else:
#        t.left(225)


t = turtle.Pen()
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

def hello():
    print('привет')

from tkinter import *
tk = Tk()
btn = Button(tk, text="нажми меня", command=hello)
btn.pack()

#window.exitonclick() # ждем нажатия кнопки

def person(width, height):
    print('Моя ширина - %s, а высота - %s' % (width, height))

person(height=3, width=4)

from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)

for x in range(0, 100):
    random_rectangle(400, 400)

window.exitonclick() # ждем нажатия кнопки
