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
    print("Running wander()")
    print("Driving Forward")
    drive(robot, log, 2, -100)
    print("Has Driven Forward")
    print("Turning")
    turn(robot, log, 90, 100)
    print("Turn Completed")
    print("Driving Forward")
    drive(robot, log, 3, 100)
    print("Has Driven Forward")
    print("Turning")
    turn(robot, log, -45, 100)
    print("Turn Completed")
    Marker = False
    print("Starting Loop")
    state = 1
    while not Marker:
        m = try_find_flag(robot)
        try:
            if m.info.marker_type == MARKER_FLAG:
                Marker = True
                print("Marker Seen")   
        except:
            if state == 1:
                drive(robot, log, 1, power)
                print("No Marker Seen")
                state = 2
            elif state == 2:
                turn(robot, log, 90, power)
                print("No Marker Seen")
                state = 3
            elif state == 3:
                turn(robot, log, 90, power)
                print("No Marker Seen")
                state = 4
            elif state == 4:
                turn(robot, log, 90, power)
                print("No Marker Seen")
                state = 5
            elif state == 5:
                turn(robot, log, 90, power)
                print("No Marker Seen")
                state = 1
        print("Finished Loop 2")
    print("Driving to Marker")
    drive_to_marker(robot, log, power)
    print("Driven to Marker")
    print("Turning 180")
    turn(robot, log, 180,  power)
    print("Turned")
    print("Retracing Steps")
    retrace(robot, log, power)
    print("Steps Retraced, Program Terminating")
    
    
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