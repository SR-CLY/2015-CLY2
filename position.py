from sr.robot import *

INITIAL_X = 0
INITIAL_Y = 0
INITIAL_BEARING = 0


class Position:
    def __init__(self, x=INITIAL_X, y=INITIAL_Y, b=INITIAL_BEARING):
        self.x = x
        self.y = y
        self.b = b


def update_position(robot, markers):
    """Gets robot location"""
    best_marker = markers[0]
    for m in markers:
        rot_y = m.centre.polar.rot_y
        if