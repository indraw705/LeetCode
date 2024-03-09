import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle you betting on choose the color ?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = []


def draw_winning_line():
    tim = Turtle()
    tim.penup()
    tim.goto(370, 250)
    tim.setheading(270)
    tim.pendown()
    tim.forward(600)


draw_winning_line()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-330, y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you won the Race !!!!")
            else:
                print(f"you lost the race winner is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
