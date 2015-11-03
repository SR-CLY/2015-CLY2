from sr.robot import *
from movement import *
from vision import *
from position import *

LEFT = -1
RIGHT = 1

"""Contains functions for strategy"""
	
def drive_to_marker(robot, log, power):
    """Drives to nearest marker"""
    print("Drive to marker")
    marker = find_flag(robot)
    drive_to(robot, log, marker, power)
    
    
def half_drive_to_marker(robot, log, power):
    marker = find_flag(robot)
    half_drive_to(robot, log, marker, power)
    
    
def reverse_safety_code(robot, log, power):
    print("Driving backward")
    drive(robot, log, 2, -power)
    sleep(1)
    print("Has Driven backward")
    print("Turning")
    turn(robot, log, 90, power)
    sleep(1)
    print("Turn Completed")
    print("Driving Forward")
    drive(robot, log, 2.25, power)
    sleep(1)
    print("Has Driven Forward")
    print("Turning")
    turn(robot, log, -85, power)
    sleep(1)
    print("Turn Completed")
    drive(robot, log, 4, power)
    sleep(1)


def wander(robot, log, power):
    """Drives into zone to the right"""
    reverse_safety_code(robot, log, power)
    search_marker(robot, 15, log, power)
    drive_to_marker(robot, log, power)
    retrace(robot, log, power)
    
    
def search_marker(robot, increment, log, power):
    Marker = False
    print("Starting search")
    state = 0
    attempt = 1
    while not Marker:
        m = try_find_flag(robot)
        try:
            if m.info.marker_type == MARKER_FLAG:
                Marker = True
                print("Marker Seen")   
        except:
            if state == 0:
                new_increment = increment * attempt
                print("Right")
                turn_old(robot, new_increment, RIGHT, power)
                state = 1
                attempt += 1
                sleep(1)
            else:
                new_increment = increment * attempt
                print("Left")
                turn_old(robot, -new_increment, LEFT, power)
                state = 0
                attempt += 1
                sleep(1)
    print("Exited loop")
    return m

	
def carpet_test(robot, log, power):
    drive(robot, log, 4, power)
    sleep(1)
    turn(robot, log, 90)
    
    
def drive_into_barrier(robot, log, power):
    turn(robot, log, 45)
    drive(robot, log, 5, power)
    
    
def retrace(robot, log, power):
    turn_old(robot, 180, 1, 50)
    actions = log.retrace()
    for action in actions:
        try:
            turn_old(robot,action[0],action[1],action[2])
        except IndexError:
            drive_old(robot, action[0],action[1])

            
