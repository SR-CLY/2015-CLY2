from sr.robot import *
from time import sleep

"""Contains functions for movement"""

# Left wheel = m0
# Right Wheel = m1


TRACK = 4  # Width of wheel in mm
SPEED = 580  # Speed in mm/s
RIGHT_COMPENSATION = 0.944
FULL_TURN = 1.975  # Seconds
FULL_MOVE = 40 #cm in 1 seconds fully powered movement.

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
    brake(robot)


def turn(robot, angle, direction, power=100):
    """Turn the robot on the spot."""
    duration = (angle + 30) * (FULL_TURN/360)
    duration = abs(duration)
    print(duration)
    if direction == RIGHT:
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
    turn(robot, angle, LEFT, power)
    while distance > 0.1:
        set_motor_power(robot, power)
    brake(robot)


def drive_towards(robot, time, angle, power):
    """Drives in a direction for specified time"""
    turn(robot, angle, power)
    drive(robot, time, power)


def release_marker(robot, power):
    turn(robot, 180, power)
    drive(robot, 1, -power)
    turn(robot, 180, power)
