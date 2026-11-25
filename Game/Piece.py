# Struct for game piece
import numpy

class Piece:
    def __init__(self, pos):
        self.pos = pos # Array of positions for each cell in piece
        self.offset = 10 # TODO: 10?

    def shiftDown(self):
        for i, pos in enumerate(self.pos):
            self.pos[i] = (pos[0], pos[1] + self.offset) # Shift y down
        return self

    def shiftLeft(self):
        for i, pos in enumerate(self.pos):
            self.pos[i] = (pos[0] - self.offset, pos[1])
        return self

    def shiftRight(self):
        for i, pos in enumerate(self.pos):
            self.pos[i] = (pos[0] + self.offset, pos[1])
        return self

    def rotate(self):
        # TODO: Right now just left
        self.pos = numpy.rot90(self.pos)
        return self

    # Equal if positions are same
    def __eq__(self, other):
        if other.pos == self.pos:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    # Comparision based on elevation
    def __lt__(self, other):
        bottom = min([self.pos[i][1] for i in range(len(self.pos))])
        other_bottom = min([other.pos[i][1] for i in range(len(self.pos))])
        return bottom < other_bottom

    def __gt__(self, other):
        bottom = min([self.pos[i][1] for i in range(len(self.pos))])
        other_bottom = min([other.pos[i][1] for i in range(len(self.pos))])
        return bottom > other_bottom

    def __le__(self, other):
        bottom = min([self.pos[i][1] for i in range(len(self.pos))])
        other_bottom = min([other.pos[i][1] for i in range(len(self.pos))])
        return bottom <= other_bottom
    
    def __ge__(self, other):
        bottom = min([self.pos[i][1] for i in range(len(self.pos))])
        other_bottom = min([other.pos[i][1] for i in range(len(self.pos))])
        return bottom >= other_bottom

    # Hash function
    def __hash__(self):
        return hash(id(self))