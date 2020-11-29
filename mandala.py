import turtle
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


for i in range(300):
    turtle.pensize(6)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.left(7)
    change_color()

done()
