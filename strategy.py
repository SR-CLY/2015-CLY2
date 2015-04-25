from sr.robot import *
from movement import *
from vision import *
from position import *

"""Contains functions for strategy"""
	
def drive_to_marker(robot, log, power):
    """Drives to nearest marker"""
    print("Drive to marker")
    marker = find_flag(robot)
    drive_to(robot, log, marker, power)

def wander(robot, log, power):
    '''Drives into zone to the right'''
    drive(robot, log, 2, -100)
    turn(robot, log, 90, 100)
    drive(robot, log, 3, 100)
    turn(robot, log, -45, 100)
    Marker = False
    while not Marker:
        m = try_find_flag(robot)
        if m.info.marker_type != MARKER_FLAG:
            drive(robot, log, 1, 100)
        else:
            Marker = True
    drive_to_marker(robot, log, power)
    retrace(robot, log, power)
    


def carpet_test(robot, log, power):
    drive(robot, log, 4, power)
    sleep(1)
    turn(robot, log, 90)
    
def drive_into_barrier(robot, log, power):
    turn(robot, log, 45)
    drive(robot, log, 5, power)
    
def retrace(robot, log, power):
    actions = log.retrace()
    for action in actions:
        try:
            turn_old(robot,action[0],action[1],action[2])
        except IndexError:
            drive_old(action[0],action[1])