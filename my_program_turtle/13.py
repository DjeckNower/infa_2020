import turtle
import math

"""
эта функция рисует окружность, по сути это 50-ти угольник
radius - радиус окружности
по умолчанию радиус 30
"""
def circle(radius = 30):
    for bla_bla in range(50):
        turtle.forward(2 * radius * math.sin(math.pi / 50))
        turtle.left(360/50)

def half_circle(radius):
    for bla_bla in range(40):
        turtle.forward(2 * radius * math.sin(math.pi / 80))
        turtle.left(360/80)

turtle.left(180)
circle
