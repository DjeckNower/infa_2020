#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    i = 1
    move_right()
    move_down()
    fill_cell()
    while True:
        move_down()
        i += 1
        k = 0
        while i != k:
            k += 1
            fill_cell()
            move_right()
        move_left(i)
        fill_cell()
        if i == 13:
            move_down()
            break
        


if __name__ == '__main__':
    run_tasks()
