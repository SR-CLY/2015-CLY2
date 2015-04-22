from sr.robot import *
from time import sleep

"""Contains functions for movement"""

# Left wheel = m0
# Right Wheel = m1


TRACK = 4  # Width of wheel in mm
SPEED = 580  # Speed in mm/s
RIGHT_COMPENSATION = 0.96 # Multiplier used to counter the effects of the right motor being more powerful 
FULL_TURN = 1.975  # Seconds
CARPET_CONSTANT = 0 # Varies with thickness of carpet/ type of surface
DISTANCE_TRAVELLED_SECOND = 0.4 #Distance in metres travelled per second

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
    """Halves motors power before stopping"""
    robot.motors[0].m0.power /= 2
    robot.motors[0].m1.power /= 2
    sleep(0.1)
    stop(robot)


def drive(robot, time, power=100):
    """Drives forward for specified time"""
    set_motor_power(robot, power)
    sleep(time)
    stop(robot)


def drive_distance(robot, distance, power=100):
    """Drives forward to a specified distance"""
    duration = abs(distance/DISTANCE_TRAVELLED_SECOND)
    drive(robot, duration, power)

def turn(robot, angle, power=100):
    """Turn the robot on the spot."""
    direction = RIGHT
    if angle >= CARPET_CONSTANT:
        angle += CARPET_CONSTANT
    duration = angle * (FULL_TURN/360)
    if duration < 0:
        direction == LEFT
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
    set_motor_power(robot, 0)


def drive_to(robot, marker, power=100):
    """Drives to a specified marker"""
    distance = marker.centre.polar.length
    angle = marker.centre.polar.rot_y
    turn(robot, angle, power)
    drive_distance(robot, distance, power)

def drive_triangle(robot, marker, power=100):
    """Drives to a sepcified marker using triangles"""
    distance = marker.centre.polar.length
    angle1 = 90 - marker.centre.polar.rot_y
    

def drive_towards(robot, time, angle, power):
    """Drives in a direction for specified time"""
    turn(robot, angle, power)
    drive(robot, time, power)


def release_marker(robot, power):
    """Releases a marker"""
    turn(robot, 180, power)
    drive(robot, 1, -power)
    turn(robot, 180, power)
