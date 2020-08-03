import math
import turtle


"""
line - начальная длинна "палки"
angle - начальный угол
"""
def arhimed():
    line = 0
    angle = 0
    while True:
        turtle.goto(line * math.sin(angle), line * math.cos(angle))
        line += 0.05
        angle += 0.05
arhimed()
