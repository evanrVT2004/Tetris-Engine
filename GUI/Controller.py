# Controller based on user inputs
# Model: Game
# View: GUI

# TODO: Right now assumes always a piece
# TODO: Add possible game states

import tkinter as tk

class Controller():

    def __init__(self, window, model, view):
        super().__init__()

        self.window = window
        self.model = model
        self.view = view

        # DEBUG:
        # Start timer
        self.downPieceTimer = 1000
        self.downPieceTimerId = self.window.after(self.downPieceTimer, self.down_arrow, None) 

    # Left arrow
    def left_arrow(self, event):
        self.model.shiftLeftPiece(self.model.currentPiece)
        self.view.clear()
        self.view.showPieces(self.model.pieces)

    def right_arrow(self, event):
        self.model.shiftRightPiece(self.model.currentPiece)
        self.view.clear()
        self.view.showPieces(self.model.pieces)

    def down_arrow(self, event):
        #self.model.move_down()
        # DEBUG
        self.window.after_cancel(self.downPieceTimerId) # Cancel previous timer
        self.model.shiftDownPiece(self.model.currentPiece)
        self.view.clear()
        self.view.showPieces(self.model.pieces)

        # DEBUG
        # Start new timer
        self.downPieceTimerId = self.window.after(self.downPieceTimer, self.down_arrow, None)

    def up_arrow(self, event):
        self.model.rotatePiece(self.model.currentPiece)
        self.view.clear()
        self.view.showPieces(self.model.pieces)

    def space(self):
        self.model.place()

    