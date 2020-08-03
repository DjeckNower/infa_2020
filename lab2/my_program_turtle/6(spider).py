import turtle

"""
numbers_sticks - количество
"""
def spider(numbers_sticks, length_stick):
    for x in range(numbers_sticks):
        turtle.forward(length_stick)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(length_stick)
        turtle.left(180)
        turtle.left(360 / numbers_sticks)

spider(100, 150)
        
