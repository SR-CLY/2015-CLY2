class Logger():
    def __init__(self):
        self.list = []
        self.list_reversed = []

    def move(self, duration, power):
        movement = (duration, power)
        self.list.append(movement)

    def turn(self, angle, direction, power):
        if direction == 1:
            direction = -1
        else:
            direction = 1
        movement = (angle, direction, power)
        self.list.append(movement)

    def retrace(self):
        self.list_reversed = self.list[::-1]
        self.list = []
        return self.list_reversed

    def clear(self):
        self.list = []