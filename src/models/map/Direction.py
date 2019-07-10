import math


class Direction:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def revert(self):
        new_x = 0
        new_y = 0
        if self.x != 0:
            new_x = self.x * -1
        if self.y != 0:
            new_y = self.y * -1
        return Direction(new_x, new_y)

    def is_parallel(self, other):
        return (-1 * other.x == self.x and -1 * other.y == self.y) or \
               (-1 * other.x == self.x and other.y == self.y) or \
               (other.x == self.x and -1 * other.y == self.y) or \
               (other == self)

    def is_perpendicular(self, other):
        return other.x - self.x == math.fabs(1) and other.y - self.y == math.fabs(1) or \
               self.x == other.x and other.y - self.y == math.fabs(2) or \
               other.x - self.x == math.fabs(2) and self.y == other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

