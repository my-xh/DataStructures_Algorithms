# -*- coding: utf-8 -*-

import turtle

pen = turtle.Pen()
pen.speed(0)
screen = turtle.Screen()

color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']


def draw_triangle(a, b, c, color='black'):
    pen.color(color)
    pen.up()
    pen.goto(a)
    pen.down()
    pen.begin_fill()
    pen.goto(b)
    pen.goto(c)
    pen.goto(a)
    pen.end_fill()


def mid_of_points(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(a, b, c, degree):
    color = color_map[degree % len(color_map)]
    draw_triangle(a, b, c, color)
    if degree > 0:
        sierpinski(a, mid_of_points(a, b), mid_of_points(a, c), degree - 1)
        sierpinski(b, mid_of_points(b, a), mid_of_points(b, c), degree - 1)
        sierpinski(c, mid_of_points(c, a), mid_of_points(c, b), degree - 1)


if __name__ == '__main__':
    a, b, c = (-500, -250), (0, 500), (500, -250)
    sierpinski(a, b, c, 5)
    screen.exitonclick()
