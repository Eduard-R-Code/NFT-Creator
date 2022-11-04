# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random



turty = turtle_module.Turtle()

turtle_module.colormode(255)

color_list = [(153, 73, 47), (170, 152, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 119, 88), (198, 92, 71), (16, 97, 75), (99, 73, 76), (67, 47, 41), (147, 178, 148), (164, 142, 155), (234, 177, 165), (55, 46, 49), (128, 29, 32), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (33, 76, 83), (47, 65, 83), (216, 177, 181), (20, 69, 62), (108, 123, 151)]
turty.penup()

turty.setheading(225)
turty.forward(300)
turty.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    turty.dot(20, random.choice(color_list))
    turty.forward(50)

    if dot_count % 10 == 0:
        turty.setheading(90)
        turty.forward(50)
        turty.setheading(180)
        turty.forward(500)
        turty.setheading(0)






screen = turtle_module.Screen()
screen.exitonclick()