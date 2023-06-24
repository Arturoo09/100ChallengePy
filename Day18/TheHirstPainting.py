# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

import turtle as t
import random

myTurtle = t.Turtle()
myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.speed(9)
myTurtle.setheading(215)
myTurtle.forward(350)
myTurtle.setheading(0)
myTurtle.hideturtle()
num_of_dots = 100


colors_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
               (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
               (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
               (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
               (174, 94, 97), (176, 192, 209)]


def random_color():
    color = random.choice(colors_list)
    color_str = '#%02x%02x%02x' % color
    return color_str


for dot_count in range(1, num_of_dots + 1):
    myTurtle.dot(40, random_color())
    myTurtle.forward(75)

    if dot_count % 10 == 0:
        myTurtle.setheading(90)
        myTurtle.forward(50)
        myTurtle.setheading(180)
        myTurtle.forward(750)
        myTurtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
