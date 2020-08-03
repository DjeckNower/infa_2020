#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    k = 1
    while k != 7:
        count = 0
        move_right(k)
        fill_cell()
        k += 1
    move_right(7)
    fill_cell()
    while not wall_is_on_the_right():
        move_right()



if __name__ == '__main__':
    run_tasks()
