from sr.robot import *
from movement import *
from vision import *
from position import *
from logger import *

log = Logger()
"""Contains functions for strategy"""
	
def drive_to_marker(robot, power):
    """A function to test things in"""
    print("Drive to marker")
    marker = find_flag(robot)
    drive_to(robot, marker, power)
    
def carpet_test(robot, power):
    drive(robot, 4, power)
    sleep(1)
    turn(robot, 90)
    
def drive_into_barrier(robot, power):
    turn(robot, 45)
    drive(robot, 5, power)
    
def retrace(robot, power):
    actions = log.retrace()
    for action in actions:
        try:
            turn(action[0],action[1],action[2])
        except IndexError:
            move(action[0],action[1])