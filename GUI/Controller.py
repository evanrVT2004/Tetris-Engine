# Controller based on user inputs
# Model: Game
# View: GUI

# TODO: Right now assumes always a piece
# TODO: Add possible game states

class Controller():

    def __init__(self, model, view):
        self.model = model
        self.view = view


    # Left arrow
    def left_arrow(self):
        self.model.move_left() # TODO: Make function in Game

    def right_arrow(self):
        self.model.move_right() # TODO: Make function in Game

    def down_arrow(self):
        self.model.move_down()

    def up_arrow(self):
        self.model.rotate_left()

    def space(self):
        self.model.place()

    