import graph

def clouds(x1, y1, radius):
    graph.penColor("black")
    graph.brushColor("white")
    graph.circle(x1 + 2*radius, y1, radius)
    graph.circle(x1 - 2*radius, y1, radius)
    graph.circle(x1 - radius, y1 - radius, radius)
    graph.circle(x1 + radius, y1 + radius, radius)
    graph.circle(x1 - radius, y1 + radius, radius)
    graph.circle(x1 + radius, y1 - radius, radius)
    graph.circle(x1, y1, radius)
    
def background(h1, h2, h3):
    graph.penColor("cyan")
    graph.brushColor("cyan")
    graph.rectangle(0, 0, 500, h1)
    graph.penColor("blue")
    graph.brushColor("blue")
    graph.rectangle(0, h1, 500, h1 + h2)
    graph.penColor("yellow")
    graph.brushColor("yellow")
    graph.rectangle(0, h1 + h2, 500, h1 + h2 + h3)
    
def sun(x, y, radius):
    graph.penColor("yellow")
    graph.brushColor("yellow")
    graph.circle(x, y, radius)

def quadrant(x, y, radius):
    graph.penSize(0)
    graph.brushColor("brown")
    graph.circle(x, y, radius)
    graph.brushColor("blue")
    graph.rectangle(x - radius, y - radius, x, y)
    graph.rectangle(x, y - radius, x + radius + 1, y + radius + 1)

def zont(x1, y1, x2, y2):
    graph.brushColor("brown")
    graph.rectangle(x1, y1, x2, y2)
    graph.brushColor("orange")
    graph.polygon([(x2 - x1, y2 + 10), (x2 - x1, y2 - 20), (x2 + 30, y2 - 20),
                   (x2 - x1, y2 + 10)])
    graph.polygon([(x2 - x1, y2 + 10), (x2 - x1, y2 - 20), (x1 - 30, y2 - 20),
                   (x2 - x1, y2 + 10)])
    

background(300, 100, 200)
sun(400, 100, 45)
clouds(100, 100, 20)
quadrant(200, 330, 30)
graph.brushColor("brown")
graph.penSize(0)
graph.rectangle(200, 330, 350, 361)   
graph.polygon([(350, 330), (350, 360), (400, 330), (350, 330)])
graph.brushColor("black")
graph.rectangle(230, 330, 240, 200)
graph.brushColor("violet")
graph.polygon([(240, 200), (275, 275), (380, 275), (240, 200)])
graph.polygon([(240, 330), (275, 275), (380, 275), (240, 330)])
