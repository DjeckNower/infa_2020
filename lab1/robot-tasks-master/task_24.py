#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def dagger():
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_right()
        fill_cell()
        move_left(2)
        fill_cell()
        move_up()
        
    move_down()
    move_right()
    dagger()
    


if __name__ == '__main__':
    run_tasks()
