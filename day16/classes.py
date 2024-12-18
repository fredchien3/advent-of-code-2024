class Position:
    def __init__(self, pos, direction, weight):
        self.pos = pos
        self.direction = direction
        self.weight = weight
        self.id = (pos[0], pos[1], direction)

    def __repr__(self):
        return 'p' + str(self.id) + str(self.weight)

    def pos(self):
        return self.pos

    def direction(self):
        return self.direction

    def weight(self):
        return self.weight

    def id(self):
        return self.id