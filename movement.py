from sr.robot import *
from time import sleep

"""Contains functions for movement"""

# Left wheel = m0
# Right Wheel = m1


TRACK = 4  # Width of wheel in mm
SPEED = 580  # Speed in mm/s
RIGHT_COMPENSATION = 0.978 # Multiplier used to counter the effects of the right motor being more powerful 
FULL_TURN = 1.885  # Seconds
CARPET_CONSTANT = 0# Varies with thickness of carpet/ type of surface
DISTANCE_TRAVELED_SECOND = 0.4 #Distance in metres traveled per second

LEFT = -1
RIGHT = 1


def set_motor_power(robot, power, motor=3):
    """Sets motors to specified power"""
    if motor == 3:
        robot.motors[0].m0.power = power
        robot.motors[0].m1.power = power * RIGHT_COMPENSATION
    elif motor == 0:
        robot.motors[0].m0.power = power
    elif motor == 1:
        robot.motors[0].m1.power = power * RIGHT_COMPENSATION


def stop(robot):
    """Stops robot immediately"""
    set_motor_power(robot, 0)


def brake(robot):
    """Sets the motors power negative before stopping"""
    robot.motors[0].m0.power = -(robot.motors[0].m0.power)
    robot.motors[0].m1.power = -(robot.motors[0].m1.power)
    stop(robot)


def drive(robot, log, time, power=100):
    """Drives forward for specified time"""
    set_motor_power(robot, power)
    sleep(time)
    brake(robot)
    log.move(time, power)

def drive_old(robot, time, power=100):
    set_motor_power(robot, power)
    sleep(time)
    brake(robot)


def drive_distance(robot, log, distance, power=100):
    """Drives forward to a specified distance"""
    duration = abs(distance/DISTANCE_TRAVELED_SECOND)
    drive(robot, log, duration, power)


def turn(robot, log, angle, power=100):
    """Turn the robot on the spot."""
    direction = RIGHT
    if angle >= CARPET_CONSTANT:
        angle += CARPET_CONSTANT
    duration = angle * (FULL_TURN/360)
    if duration < 0:
        direction = LEFT
        print("LEFT")
    duration = abs(duration)
    print(duration)
    if direction == RIGHT:
        print("RIGHT")
        set_motor_power(robot, power, 0)
        set_motor_power(robot, -power, 1)
    else:
        set_motor_power(robot, -power, 0)
        set_motor_power(robot, power, 1)
    sleep(duration)
    brake(robot)
    log.turn(angle, direction, power)
    
    
def turn_old(robot, angle, direction, power=100):
    """Required for Logger class to work correctly"""
    if angle >= CARPET_CONSTANT:
        angle += CARPET_CONSTANT
    duration = abs(angle * (FULL_TURN/360))
    if direction == RIGHT:
        print("RIGHT")
        set_motor_power(robot, power, 0)
        set_motor_power(robot, -power, 1)
    else:
        set_motor_power(robot, -power, 0)
        set_motor_power(robot, power, 1)
    sleep(duration)
    brake(robot)
    
def drive_to(robot, log, marker, power=100):
    """Drives to a specified marker"""
    distance = marker.centre.polar.length
    angle = marker.centre.polar.rot_y
    turn(robot, log, angle, power)
    drive_distance(robot, log, distance, power)

def drive_triangle(robot, marker, power=100):
    """Drives to a sepcified marker using triangles"""
    distance = marker.centre.polar.length
    angle1 = 90 - marker.centre.polar.rot_y
    

def drive_towards(robot, log, time, angle, power):
    """Drives in a direction for specified time"""
    turn(robot, log, angle, power)
    drive(robot, log, time, power)


def release_marker(robot, power):
    """Releases a marker"""
    turn_old(robot, 180, 1, power)
    drive_old(robot, 1, -power)
    turn_old(robot, 180, 1, power)
