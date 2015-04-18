from sr.robot import *
from time import sleep
from movement import *
from vision impport *

"""Main File"""

R = Robot()


def test(robot, power):
    """A function to test things in"""
    print("test")
    marker = find_flag(robot)
    drive_to(robot, marker, power)

test(R, 100)

stop(R)
