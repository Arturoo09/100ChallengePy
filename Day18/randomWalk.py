import turtle as t
import random

myTurtle = t.Turtle()
myTurtle.shape("turtle")
myTurtle.width(10)
myTurtle.speed(9)

directions = [0, 90, 180, 270]


def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    random_color = (r, b, g)
    return random_color


def random_direction():
    distance = random.randint(30, 100)
    if (-300 < myTurtle.xcor() < 300) and (-300 < myTurtle.ycor() < 300):
        myTurtle.right(random.choice(directions))
        myTurtle.forward(distance)
    else:
        myTurtle.right(180)
        myTurtle.forward(distance)


def draw_walk():
    for _ in range(50):
        myTurtle.color(random_colors())
        random_direction()
        myTurtle.forward(10)


draw_walk()

screen = t.Screen()
screen.exitonclick()
