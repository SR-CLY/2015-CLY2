from sr.robot import *
from time import sleep
from strategy import *
from logger import *
log = Logger()

"""Main File"""

R = Robot()

def stage_one(robot, log, power):
    drive_to_marker(robot, log, power)
    drive(robot, log, 1, power)
    release_marker(robot, power)
    
def saftey_code(robot,log, power):
    drive_distance(robot, log, 2, power)
    turn(robot, log, 45, power)
    drive(robot,log, 3, power)

def test(robot, log, power):
    stage_one(robot, log, power)

test(R, log, 100)

