from sr.robot import *
from time import sleep
from movement import *

"""Main File"""

R = Robot()


def test(robot, power):
    """A function to test things in"""
    print("test")
    drive(robot, 4, power)

test(R, 100)

stop(R)
