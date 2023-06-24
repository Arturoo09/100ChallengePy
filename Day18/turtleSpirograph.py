import turtle as t
import random

myTurtle = t.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)


def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = '#%02x%02x%02x' % (r, g, b)
    return color


def draw_circle():
    myTurtle.color(random_colors())
    myTurtle.circle(100)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        draw_circle()
        myTurtle.setheading(myTurtle.heading() + size_of_gap)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
