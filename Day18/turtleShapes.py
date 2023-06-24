import turtle as t
import random

myTurtle = t.Turtle()
myTurtle.shape("turtle")


def random_colors():
    R = random.random()
    B = random.random()
    G = random.random()

    myTurtle.color(R, G, B)


def draw_shape(num_of_sides):
    myTurtle.forward(100)
    myTurtle.right(360 / num_of_sides)


for sides in range(3, 11):
    random_colors()
    for _ in range(sides):
        draw_shape(sides)

screen = t.Screen()
screen.exitonclick()
