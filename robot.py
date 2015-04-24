from sr.robot import *
from time import sleep
from strategy import *
from logger import *
log = Logger()

"""Main File"""

R = Robot()

def stage_one(robot, log, power):
    """Moves forward to first marker, pushes into zone and then releases it"""
    drive_to_marker(robot, log, power)
    drive(robot, log, 1, power)
    release_marker(robot, power)
    print(log.retrace)
    
def saftey_code(robot,log, power):
    """Hardcoded to drive first marker into wall"""
    drive_distance(robot, log, 2, power)
    turn(robot, log, 45, power)
    drive(robot,log, 3, power)

def test(robot, log, power):
    """A test function"""
    saftey_code(robot, log, power)

test(R, log, 100)

