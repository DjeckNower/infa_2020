import turtle


"""
line - длина начальной линии
a - сколько прибавляется длинны за шаг
b - сколько линий рисуется
"""
def sqar_spiral(line, a, b):
    for x in range(b):
        line += a
        turtle.forward(line)
        turtle.left(90)
        
sqar_spiral(1, 10, 100) 
        

    
