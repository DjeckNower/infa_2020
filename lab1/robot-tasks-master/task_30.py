#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    i = -1
             
    while not wall_is_beneath():
        move_down()
        i += 1
    while i > 0:
        k = 0
        while k != i:
            move_right()
            fill_cell()
            k += 1
        move_right()
        k = 0
        while k != i:
            move_up()
            fill_cell()
            k += 1
        move_up()
        k = 0
        while k != i:
            move_left()
            fill_cell()
            k += 1
        move_left()
        k = 0
        while k != i:
            move_down()
            fill_cell()
            k += 1
        move_down()
        move_right()
        move_up()
        i -= 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()
    


if __name__ == '__main__':
    run_tasks()
