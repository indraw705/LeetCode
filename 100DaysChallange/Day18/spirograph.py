import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

tim = Turtle()
# tim.shape("turtle")
tim.speed(50)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
