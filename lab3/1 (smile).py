import graph

graph.penColor("black")
graph.brushColor("yellow")
graph.circle(250, 250, 200)

graph.brushColor("red")
graph.circle(175, 200, 50)
graph.circle(325, 200, 40)

graph.brushColor("black")
graph.circle(175, 200, 20)
graph.circle(325, 200, 20)

graph.polygon([(230, 200), (227, 175), (50, 45), (35, 35)])

y1 = -30
graph.polygon([(285, 210 + y1), (275, 200 + y1), (400, 65 + y1), (410, 75 + y1)])

graph.polygon([(175, 350), (325, 350), (325, 400), (175, 400)])
