from sr.robot import *
from time import sleep
from movement import *
from vision import *

"""Main File"""

R = Robot()


def drive_to_marker(robot, power):
    """A function to test things in"""
    print("Drive to marker")
    marker = find_flag(robot)
    drive_to(robot, marker, power)

def stage_one(robot, power):
    drive_to_marker(robot, power)
    drive(robot, 1, power)
    release_marker(robot, power)


stage_one(R, 100)

stop(R)
