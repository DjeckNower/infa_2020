#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while True:
        if not wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            fill_cell()
            move_right()
        elif not wall_is_on_the_right():
            move_right()
        elif not wall_is_above() and wall_is_beneath():
            fill_cell()
            break
        else:
            break

if __name__ == '__main__':
    run_tasks()
