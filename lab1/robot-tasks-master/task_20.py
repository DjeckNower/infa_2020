#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i = 0
    while True:
        move_right()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        i += 1
        if i == 12:
            break
        move_down()
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        i += 1
        move_down()
        if i == 12:
            break
    move_right()



    
if __name__ == '__main__':
    run_tasks()
