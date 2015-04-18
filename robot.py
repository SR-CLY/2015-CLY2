from sr.robot import *
from time import sleep
from movement import *
from vision import *

"""Main File"""

R = Robot()


def test(robot, power):
    """A function to test things in"""
    print("test")
    turn(robot, 180, 0, power)
    #marker = find_flag(robot)
    #drive_to(robot, marker, power)
        

test(R, 100)

stop(R)
