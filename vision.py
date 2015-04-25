from sr.robot import *

"""Contains functions for vision"""


def find_flag(robot):
    """Returns first flag it sees"""
    Marker = False
    while not Marker:
        markers = robot.see()
        for m in markers:
            print("Marker is type {} and distance {} and rot {}".format(m.info.marker_type, m.dist, m.centre.polar.rot_y))
            if m.info.marker_type == MARKER_FLAG:
                return m
                Marker = True
                
def try_find_flag(robot):
    """Tries to return a flag marker"""
    markers = robot.see()
    for m in markers:
        print("Marker is type {} and distance {} and rot {}".format(m.info.marker_type, m.dist, m.centre.polar.rot_y))
        if m.info.marker_type == MARKER_FLAG:
            return m


def find_robot(robot):
    """Returns first robot it sees"""
    markers = robot.see()
    for m in markers:
        print("Marker is type {} and distance {}".format(m.info.marker_type, m.dist))
        if m.info.marker_type == MARKER_ROBOT:
            return m


def find_wall(robot):
    """Returns first arena flag it sees"""
    markers = robot.see()
    for m in markers:
        print("Marker is type {} and distance {}".format(m.info.marker_type, m.dist))
        if m.info.marker_type == MARKER_ARENA:
            return m


def find_walls(robot):
    """Returns list of wall markers"""
    markers = robot.see()
    wall_markers = []
    for m in markers:
        if m.info.marker_type == MARKER_ARENA:
            wall_markers.append(m)
    return wall_markers