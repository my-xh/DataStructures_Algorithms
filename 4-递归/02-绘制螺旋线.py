# -*- coding: utf-8 -*-

import turtle

pen = turtle.Pen()
pen.speed(0)
screen = turtle.Screen()


def draw_spiral(length):
    if length > 0:
        pen.forward(length)
        pen.right(90)
        draw_spiral(length - 5)


if __name__ == '__main__':
    draw_spiral(100)
    screen.exitonclick()
