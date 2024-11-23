# Первый урок программирования на Phyton

import turtle
#window = turtle.Screen()
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

for i in range(10):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()


#window.exitonclick() # ждем нажатия кнопки