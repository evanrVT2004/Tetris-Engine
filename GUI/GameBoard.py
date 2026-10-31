

## Game Board Code for the Tetris Engine ##


class GameBoard:

    ## Initialize the Game Board with a Given Width and Height ##
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    ## Check If a Cell is Empty (If a Cell is Empty, return true(0) else return false(1)) ##
    def is_empty(self, row, column):
        return(self.grid[row][column] == 0)

    ## Check If a Row is Full (If a Row is Full, return true(1) else return false(0)) ##
    def is_full(self, row, column):
        return(self.grid[row][column] == 1)
