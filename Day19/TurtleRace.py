import turtle as t
from random import randint

is_race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("BET", "What color is going to win??")
colors = ["red", "orange", "purple", "yellow", "green", "blue"]
all_turtles = []


cord_y = -70
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=cord_y)
    cord_y += 30
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet! Winning color: {winning_color}.")
            else:
                print(f"You've lost the bet! Winning color: {winning_color}.")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
