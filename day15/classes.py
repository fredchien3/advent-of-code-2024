class Object:
    def __init__(self, pos):
        self.pos = pos

class MovableObject(Object):
    def move(self, delta):
        y, x = self.pos
        dy, dx = delta
        self.pos = (y + dy, x + dx)

class Robot(MovableObject):
    def __str__(self):
        return '@'

class Box(MovableObject):
    def __str__(self):
        return 'O'

    def get_score(self):
        y, x = self.pos
        return (100 * y) + x

class Wall(Object):
    def __str__(self):
        return '#'