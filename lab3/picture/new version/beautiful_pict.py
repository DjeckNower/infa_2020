import graph

def backgroung(length_sky):
    #sky
    graph.penSize(0)
    graph.brushColor("skyblue")
    #grass
    graph.rectangle(0, 0, 500, length_sky)
    graph.brushColor("limegreen")
    graph.rectangle(0, length_sky, 500, 600)

"""
bottom_tree_x and bottom_tree_y it's center barrel down
"""
def tree(bottom_tree_x, bottom_tree_y, barrel_length):
    #barrel
    graph.penColor("black")
    graph.brushColor("black")
    graph.rectangle(bottom_tree_x - barrel_length/16, bottom_tree_y,
                    bottom_tree_x + barrel_length/16, bottom_tree_y - barrel_length)
    #leaves
    graph.penSize(1)
    graph.penColor("black")
    graph.brushColor("green")
    graph.circle(bottom_tree_x, bottom_tree_y - (barrel_length + barrel_length/1.75), barrel_length/4)
    graph.circle(bottom_tree_x - barrel_length/3, bottom_tree_y - (barrel_length + barrel_length/3), barrel_length/4)
    graph.circle(bottom_tree_x + barrel_length/3, bottom_tree_y - (barrel_length + barrel_length/3), barrel_length/4)
    graph.circle(bottom_tree_x, bottom_tree_y - (barrel_length + barrel_length/5), barrel_length/4)
    graph.circle(bottom_tree_x - barrel_length/4, bottom_tree_y - barrel_length, barrel_length/4)
    graph.circle(bottom_tree_x + barrel_length/4, bottom_tree_y - barrel_length, barrel_length/4)

def clouds(x1, y1, radius):
    graph.penColor("black")
    graph.brushColor("white")
    graph.circle(x1, y1 - 1.5 * radius, radius)
    graph.circle(x1, y1 + 1.5 * radius, radius)
    graph.circle(x1 + 2*radius, y1, radius)
    graph.circle(x1 - 2*radius, y1, radius)
    graph.circle(x1 - radius, y1 - radius, radius)
    graph.circle(x1 + radius, y1 + radius, radius)
    graph.circle(x1 - radius, y1 + radius, radius)
    graph.circle(x1 + radius, y1 - radius, radius)
    graph.circle(x1, y1, radius)
    

def home(center_x, center_y, side_length):
    #side
    graph.penSize(1)
    graph.penColor("black")
    graph.brushColor("peru")
    graph.rectangle(center_x - side_length/2, center_y + side_length/2,
                    center_x + side_length/2, center_y - side_length/2)
    #window
    graph.penColor("red")
    graph.brushColor("aqua")
    graph.rectangle(center_x - side_length/8, center_y + side_length/8,
                    center_x + side_length/8, center_y - side_length/8)
    #roof
    graph.penColor("black")
    graph.brushColor("red")
    graph.polygon([(center_x + side_length/2, center_y - side_length/2),
                    (center_x - side_length/2, center_y - side_length/2),
                    (center_x, center_y - side_length),
                    (center_x + side_length/2, center_y - side_length/2)])
def purple_sun(x, y, radius):
    graph.penColor("darksalmon")
    graph.brushColor("violet")
    graph.circle(x, y, radius)
        

backgroung(300)
home(150, 400, 150)    
tree(400, 400, 100)   
clouds(200, 150, 20)
purple_sun(450, 120, 40)
