import math
import turtle


"""
эта функция рисует полу окружность, по сути это полу 80-ти угольник
radius - радиус полу окружности
"""
def half_circle(radius):
    for bla_bla in range(40):
        turtle.forward(2 * radius * math.sin(math.pi / 80))
        turtle.left(360/80)

def spring(num_turns, radius_big, radius_mini):
    for bla_bla_2 in range(num_turns):
        half_circle(radius_big)
        half_circle(radius_mini)

turtle.left(90)
spring(20, 10, 40)

