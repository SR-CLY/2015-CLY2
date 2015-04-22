from sr.robot import *
from time import sleep
from strategy import *

"""Main File"""

R = Robot()

def stage_one(robot, power):
    drive_to_marker(robot, power)
    drive(robot, 1, power)
    release_marker(robot, power)

def test(robot, power):
    carpet_test(robot, power)
    stage_one(robot, power)

test(R, 100)

