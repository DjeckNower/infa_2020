import graph

"""
НЕ ЗАБУДЬ РЕШИТЬ ПРОБЛЕМУ С ЭКРАНОМ В ФУНКЦИИ
backgroung(не закрашивает весь экран)
"""


def backgroung(length_sky):
    """
    Эта функция берёт длинну неба
    и заполняет остальное пространство кроме неба травой.
    Также она отвечает за ширину и высоту экрана
    """
    main_screen_width = 1600
    main_screen_height = 1000
    graph.windowSize(main_screen_width, main_screen_height)
    graph.penSize(0)
    graph.brushColor("skyblue")
    graph.rectangle(0, 0, main_screen_width, length_sky)
    graph.brushColor("limegreen")
    graph.rectangle(0, length_sky, main_screen_width, main_screen_height)


def tree(bottom_tree_x, bottom_tree_y, barrel_length):
    """
    bottom_tree_x and bottom_tree_y -- центральные координаты низа дерева.
    barrel_length -- высота дерева

    barrel_lengt/8 -- ширина этого дерева
    У всех шариков радиусы barrel_length/4

    Центры двух нижних шариков находятся на той же выстое,
    что и макушка дерева,
    и они на расстоянии barrel_length/4 от центральной оси симметрии.
    Их координаты:
    левая: (bottom_tree_x - barrel_length/4, bottom_tree_y - barrel_length)
    правая -- (bottom_tree_x + barrel_length/4, bottom_tree_y - barrel_length)

    Третий шарик считая снизу выше макушки дерева на barrel_length/5
    Он находится по центру
    координата x -- bottom_tree_x
    координата y -- bottom_tree_y - 6/5 * barrel_length)

    Четвёртый и пятый шарик считая снизу выше маушки дерева на barrel_length/3,
    и они на расстоянии barrel_length/3 от центральной оси симметрии
    левый шарик:
    координата x -- bottom_tree_x - barrel_length/3
    кооридината y -- bottom_tree_y - 4/3 * barrel_length)
    правый шарик:
    координата x -- bottom_tree_x + barrel_length/3,
    координата y -- bottom_tree_y - 4/3 * barrel_length)

    Наивысшый шарик выше макушки дерева на 4/7*barrel_length,
    и он расположен по центру
    координата x  -- bottom_tree_x
    координата y -- bottom_tree_y - 27 / 17 * barrel_length), barrel_length/4)

    """
    # barrel
    graph.penColor("black")
    graph.brushColor("black")
    graph.rectangle(bottom_tree_x - barrel_length / 16,
                    bottom_tree_y,
                    bottom_tree_x + barrel_length / 16,
                    bottom_tree_y - barrel_length)
    # leaves
    graph.penSize(1)
    graph.penColor("black")
    graph.brushColor("green")
    graph.circle(bottom_tree_x, bottom_tree_y - 27 / 17 * barrel_length, barrel_length / 4)
    graph.circle(bottom_tree_x - barrel_length/3, bottom_tree_y - (barrel_length + barrel_length/3), barrel_length/4)
    graph.circle(bottom_tree_x + barrel_length/3, bottom_tree_y - (barrel_length + barrel_length/3), barrel_length/4)
    graph.circle(bottom_tree_x, bottom_tree_y - (barrel_length + barrel_length/5), barrel_length/4)
    graph.circle(bottom_tree_x - barrel_length/4, bottom_tree_y - barrel_length, barrel_length/4)
    graph.circle(bottom_tree_x + barrel_length/4, bottom_tree_y - barrel_length, barrel_length/4)


def clouds(x1, y1, radius):
    """
    x1 - координата центра центральной окружности X
    y1 - координата центра центральной окружности Y
    radius - радиус шариков составляющих облако

    Центр каждого из шариков расположен на расстоянии
    2 * radius от центра окружности лежащей с ней на одной высоте

    Координаты наивысших шариков
    graph.circle(x1, y1 - 1.5 * radius, radius)
    graph.circle(x1, y1 + 1.5 * radius, radius)
    """
    graph.penColor("black")
    graph.brushColor("white")
    graph.circle(x1, y1 - 1.5 * radius, radius)
    graph.circle(x1, y1 + 1.5 * radius, radius)

    graph.circle(x1 + 2 * radius, y1, radius)
    graph.circle(x1 - 2 * radius, y1, radius)

    graph.circle(x1 - radius, y1 - radius, radius)
    graph.circle(x1 + radius, y1 + radius, radius)

    graph.circle(x1 - radius, y1 + radius, radius)
    graph.circle(x1 + radius, y1 - radius, radius)
    graph.circle(x1, y1, radius)


def home(center_x, center_y, side_length):
    # side
    graph.penSize(1)
    graph.penColor("black")
    graph.brushColor("peru")
    graph.rectangle(center_x - side_length / 2, center_y + side_length / 2,
                    center_x + side_length / 2, center_y - side_length / 2)
    # window
    graph.penColor("red")
    graph.brushColor("aqua")
    graph.rectangle(center_x - side_length / 8, center_y + side_length / 8,
                    center_x + side_length / 8, center_y - side_length / 8)
    # roof
    graph.penColor("black")
    graph.brushColor("red")
    graph.polygon([(center_x + side_length / 2, center_y - side_length / 2),
                    (center_x - side_length / 2, center_y - side_length / 2),
                    (center_x, center_y - side_length),
                    (center_x + side_length / 2, center_y - side_length / 2)])


def purple_sun(x, y, radius):
    graph.penColor("darksalmon")
    graph.brushColor("violet")
    graph.circle(x, y, radius)   


backgroung(300)
home(150, 400, 150)    
tree(300, 450, 100)
home(400, 350, 50)    
tree(450, 350, 33)
clouds(200, 120, 20)
clouds(300, 50, 20)
clouds(400, 120, 20)
purple_sun(50, 50, 40)
