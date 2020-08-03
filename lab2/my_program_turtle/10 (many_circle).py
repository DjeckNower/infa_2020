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


"""
num_petals - четное
"""
def flower(num_petals):
    for x in range(num_petals):
        circle()
        turtle.right(360/num_petals)
        
            
flower(7)   
