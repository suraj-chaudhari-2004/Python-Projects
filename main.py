from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
is_game_on = False

user_bet = screen.textinput("Make your bet", "Which color turtle will win?")
colors = ["red","orange","yellow","green","blue","purple"]
is_game_on = True

ordinate = -100
i=0

turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    i += 1
    new_turtle.penup()
    new_turtle.goto(x=-230, y = ordinate)
    ordinate += 40
    turtles.append(new_turtle)

while is_game_on:
    for turtle in turtles:
        speed = random.randint(0, 10)
        turtle.forward(speed)
        if turtle.xcor() > 230:
            is_game_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You WON! The winning turtle is {winner}")
            else:
                print(f"You lost! The winning turtle is {winner}")


screen.exitonclick()