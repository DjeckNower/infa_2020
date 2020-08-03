#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while True:
        if not wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
            move_up()
            fill_cell()
            move_down()
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif not wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_above() and not wall_is_beneath() and not wall_is_on_the_right():
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            move_right()
            
        elif not wall_is_above() and not wall_is_beneath():
            move_up()
            fill_cell()
            move_down()
            move_down()
            fill_cell()
            move_up()
            break
        elif not wall_is_above() and wall_is_beneath():
            move_up()
            fill_cell()
            move_down()
            break
        elif wall_is_above() and not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
            break
        else:
            break
            


if __name__ == '__main__':
    run_tasks()
