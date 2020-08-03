import turtle
import math

"""
эта функция может строить квадраты очень по разному
numbers_sqare - количество квадратов
length_of_the_first_square - длинна первого квадрата
increasing_the_length_of_the_square - разовое увеличение длинны квадрата
distance_between_sides_of_the_squares - расстояние между сторонами квадратов
"""
def many_sqare(numbers_sqare, length_of_the_first_square, increasing_the_length_of_the_square, distance_between_sides_of_the_squares):
    for x in range(numbers_sqare):
        for y in range(4):
            turtle.forward(length_of_the_first_square)
            turtle.left(90)
        turtle.penup()
        turtle.right(90)
        turtle.forward(distance_between_sides_of_the_squares)
        turtle.right(90)
        turtle.forward(distance_between_sides_of_the_squares)
        turtle.right(180)
        length_of_the_first_square += increasing_the_length_of_the_square
        turtle.pendown()

many_sqare(10000, 5, 5, 3)
        
    
    
    
