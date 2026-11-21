# Struct for game piece
import numpy

class Piece:
    def __init__(self, pos):
        self.pos = pos # Array of positions for each cell in piece

    def shiftDown(self):
        for i, pos in enumerate(self.pos):
            self.pos[i] = (pos[0], pos[1] + 10) # Shift y down # TODO: Offset
        return self

    def rotate(self):
        # TODO: Right now just left
        numpy.rot90(self.pos)
        return self