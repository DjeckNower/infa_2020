#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    
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

    def line_dagger():
        while True:
            dagger()
            move_right(2)
            if wall_is_on_the_right():
                while not wall_is_on_the_left():
                    move_left()
                break
            else:
                move_right(2)
            

    line_dagger()
    move_down(4)
    line_dagger()
    move_down(4)
    line_dagger()
    move_down(4)
    line_dagger()
    move_down(4)
    line_dagger()
            
        


if __name__ == '__main__':
    run_tasks()
