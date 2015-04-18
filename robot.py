from sr.robot import *
from time import sleep
from movement import *
from vision import *

"""Main File"""

R = Robot()


def test(robot, power):
    """A function to test things in"""
    print("test")
    Marker = False
    while not Marker:
        marker = find_flag(robot)
        if m.info.marker_type == MARKER_ROBOT:
            Marker = True
    drive_to(robot, marker, power)
        

test(R, 100)

stop(R)
