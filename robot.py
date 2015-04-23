from sr.robot import *
from time import sleep
from strategy import *
from logger import *
log = Logger()

"""Main File"""

R = Robot()

def stage_one(robot, log, power):
    drive_to_marker(robot, log, power)
    drive(robot, 1, power)
    release_marker(robot, power)

def test(robot, log, power):
    stage_one(robot, log, power)

test(R, log, 100)

