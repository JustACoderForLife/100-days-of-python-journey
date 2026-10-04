# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [
    (203, 172, 110),
    (152, 179, 196),
    (150, 182, 172),
    (194, 165, 176),
    (224, 200, 119),
    (206, 181, 198),
    (187, 172, 61),
    (174, 189, 213),
    (160, 207, 193),
    (162, 202, 215),
    (111, 122, 182),
    (214, 183, 179),
    (127, 127, 127),
]

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.up()
timmy.goto(-225, -225)
timmy.down()


def draw_painting(size_dots, distance, turtle, number_of_dots):
    def draw_dot():
        color = random.choice(color_list)
        turtle.dot(size_dots, color)
        turtle.up()
        turtle.forward(distance)
        turtle.down()

    def draw_row():
        for key in range(number_of_dots):
            draw_dot()

    def return_position():
        turtle.left(90)
        turtle.up()
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(number_of_dots * distance)
        turtle.right(180)

    for key in range(number_of_dots):
        draw_row()
        return_position()


draw_painting(20, 50, timmy, 10)
screen.exitonclick()
