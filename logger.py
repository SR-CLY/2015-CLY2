class Loggger():
    def __init__(self):
        self.list = []

    def move(self, duration, power):
        movement = (duration, power)
        self.list.append(movement)

    def turn(self, angle, direction, power):
        angle = -angle
        direction = -direction
        movement = (angle, direction, power)
        self.list.append(movement)

    def retrace(self):
        return self.list