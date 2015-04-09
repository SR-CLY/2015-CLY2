from sr.robot import *
from movement import *
from vision import *
from position import *
"""Contains functions for strategy"""


def get_location(robot, power):
    """Scans for wall marker with rot_y closet to 0"""
    markers = find_walls(robot)
    update_position(robot, markers)