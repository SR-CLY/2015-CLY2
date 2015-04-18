from sr.robot import *
from time import sleep
from movement import *
from vision import *

"""Main File"""

R = Robot()


def test(robot, power):
    """A function to test things in"""
    print("test")
    while True:
        marker = find_flag(robot)

test(R, 100)

stop(R)
