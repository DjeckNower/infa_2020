import math
import turtle

"""
num_side - количество сторон в многоугольнике
radius - радиус описанной окружности многоугольника
"""
def polygon(num_side, radius):
    for bla_bla in range(num_side):
        turtle.forward(2 * radius * math.sin(math.pi / num_side))
        turtle.left(360/num_side)

"""
num_polygons - количество многоугольников
n - количество сторон начального многоугольника
initial_radius - радиус начального многоугольника
plus_radius - прибавление длинны радиуса след. многоугольника

"""
def many_polygons(num_polygons, initial_radius, plus_radius):
    n = 3
    for bla_bla_2 in range(num_polygons):
        polygon(n, initial_radius)
        turtle.penup()
        turtle.right(90 + 180/n)
        turtle.forward(plus_radius)
        n += 1
        initial_radius += plus_radius
        turtle.left(90 + 180/n)
        turtle.pendown()



        
many_polygons(20, 20, 30)
        
