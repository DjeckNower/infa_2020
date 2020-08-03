import turtle
import math

def polygon(number_of_sides, length):
    for x in range(number_of_sides):
        turtle.forward(length)
        turtle.left(360 / number_of_sides)
        
polygon(5, 20)
    
