# import colorgram
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 42)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
tim.speed(50)

color_list = [(242, 243, 237), (38, 105, 156), (245, 143, 74), (238, 216, 82), (184, 153, 14), (224, 243, 230), (187, 46, 84), (149, 74, 38), (189, 67, 103), (229, 134, 174), (158, 12, 64), (10, 175, 148), (103, 192, 217), (106, 197, 155), (53, 53, 116), (252, 154, 147), (141, 212, 228), (238, 94, 55), (18, 142, 100), (226, 238, 244), (25, 87, 84), (247, 230, 235), (105, 50, 30), (57, 187, 191), (50, 44, 77), (130, 88, 176), (245, 206, 6), (99, 46, 25), (229, 166, 181), (152, 214, 196), (184, 186, 210), (30, 91, 93), (19, 74, 73), (96, 81, 30)]
tim.penup()
tim.speed(100)
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
for _ in range(1, num_of_dots+1):
    tim.pendown()
    tim.dot(21, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if _ % 10 == 0:
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
