import math
import turtle

"""
эта функция рисует окружность, по сути это 50-ти угольник
radius - радиус окружности
по умолчанию радиус 30
"""
def circle(radius = 30):
    for bla_bla in range(50):
        turtle.forward(2 * radius * math.sin(math.pi / 50))
        turtle.left(360/50)

def butterfly(num_double_circles, start_radius, plus_radius):
    for x in range(num_double_circles):
        circle(start_radius)
        turtle.left(180)
        circle(start_radius)
        start_radius += plus_radius

butterfly(10, 20, 10)
