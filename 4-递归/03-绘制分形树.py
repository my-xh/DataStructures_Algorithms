# -*- coding: utf-8 -*-

import turtle

pen = turtle.Pen()
pen.speed(0)
screen = turtle.Screen()


def tree(length):
    if length > 5:
        pen.forward(length)
        pen.right(20)
        tree(length - 15)
        pen.left(40)
        tree(length - 10)
        pen.right(20)
        pen.backward(length)


if __name__ == '__main__':
    pen.left(90)
    pen.up()
    pen.backward(300)
    pen.down()
    pen.color('green')
    tree(110)
    screen.exitonclick()
