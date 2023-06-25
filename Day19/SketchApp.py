import turtle as t

myTurtle = t.Turtle()
myTurtle.shape("turtle")


def move_down():
    myTurtle.backward(20)


def move_up():
    myTurtle.forward(20)


def turn_left():
    new_heading = myTurtle.heading() + 10
    myTurtle.setheading(new_heading)


def turn_right():
    new_heading = myTurtle.heading() - 10
    myTurtle.setheading(new_heading)


def clear():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.home()
    myTurtle.pendown()


screen = t.Screen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(turn_left, "q")
screen.onkey(turn_right, "e")
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()
