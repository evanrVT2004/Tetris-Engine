## Importing Necessary Libraries and Modules ##
import tkinter as tk
from GUI.GameBoard import GameBoard, ScoreBoard
from GUI.Controller import Controller
from Game.Game import Game
from Game.Piece import Piece

## Main Function to Display the Game Board and Score Board ##
if __name__ == "__main__":
    game_board = GameBoard()
    score_board = ScoreBoard()

    window = tk.Tk()
    window.title("|_|TETRIS|_|")

    canvas = tk.Canvas(window, width=300, height=600, bg="black")
    canvas.grid(row=0, column=0, padx=10, pady=10)
    game_board.canvas = canvas

    ## TODO: Create a Score Function to Update the Score Board ##
    score_label = tk.Label(window, text = "Score: 0", font=("Times New Roman", 18))
    score_label.grid(row=0, column=1, padx=10, pady=10)

    cell_width = 300 // game_board.width
    cell_height = 600 // game_board.height

    for row in range(game_board.height):
        for column in range(game_board.width):
            x1 = column * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, outline="grey")

    # DEBUG
    game = Game()
    controller = Controller(game, game_board)

    pos = [(0,0), (0,30), (30,0), (30,30)]
    piece = Piece(pos)
    game.addPiece(piece)
    game.currentPiece = piece
    
    window.bind("<Down>", controller.down_arrow)

    #game_board.showPieces(game.pieces, canvas)
    
    window.mainloop()
