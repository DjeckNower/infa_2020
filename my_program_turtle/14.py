import math
import turtle

def star(lenght, num_tops):
    for x in range(num_tops):
        turtle.forward(lenght)
        turtle.left(1440/num_tops)
star(50, 11)
