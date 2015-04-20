from sr.robot import *
from movement import *
from vision import *
from position import *
"""Contains functions for strategy"""

    update_position(robot, markers)    update_position(robot, markers)    update_position(robot, markers)    update_position(robot, markers)	
	
def drive_to_marker(robot, power):
    """A function to test things in"""
    print("Drive to marker")
    marker = find_flag(robot)
    drive_to(robot, marker, power)