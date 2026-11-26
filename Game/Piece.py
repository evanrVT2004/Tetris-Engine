class Piece:
    def __init__(self, pos):
        self.pos = [tuple(cell) for cell in pos]
        self.offset = 30

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
        if not self.pos:
            return self

        min_x = min(x for x, _ in self.pos)
        min_y = min(y for _, y in self.pos)
        max_x = max(x for x, _ in self.pos)
        self.pos = [
            (min_x + y - min_y, min_y + max_x - x)
            for x, y in self.pos
        ]
        return self