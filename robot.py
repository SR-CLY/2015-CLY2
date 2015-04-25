from sr.robot import *
from time import sleep
from strategy import *
from logger import *
log = Logger()

"""Main File"""

R = Robot()

def stage_one(robot, log, power):
    """Moves forward to first marker, pushes into zone and then releases it"""
    drive(robot, log, 1, power)
    release_marker(robot, power)
    drive(robot, log, 2, power)
    drive_to_marker(robot, log, power)
    turn_old(robot, 180, 1, power)
    drive(robot, log, 2, power)
    print(log.retrace)
    
def saftey_code(robot,log, power):
    """Hardcoded to drive first marker into wall"""
    drive_distance(robot, log, 1, power)
    turn(robot, log, 45, power)
    drive(robot,log, 5, power)

def two_flag_code(robot, log, power):
    '''Safety_Code() and then Wander()'''
    saftey_code(robot,log,power)
    wander(robot, log, power)

def test(robot, log, power):
    """A test function"""
    stage_one(robot, log, power)

two_flag_code(R, log, 100)

