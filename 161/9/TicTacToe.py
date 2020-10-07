# project-9
# Author: Craig Sperlazza
# Date: 11/14/2019
# Description: Creates a TicTacToe class that has two private data members:
# board and current state, together with a method that allows the
# player to make moves and keeps track of the current game data, such as
# if the game is finished, draw, won, etc.


class TicTacToe:
    """Class named TicTacToe that has two private data members: the board,
    and the current state of the game, which will update to alert if either
    x or o have won the game or if it is a draw"""

    def __init__(self):
        """Initializes a tic-tac-toe board as a list made of three list elements
        and sets the current state of the game to unfinished"""
        self._board = [["","",""], ["","",""], ["","",""]]
        self._current_state = "UNFINISHED"


    def get_current_state(self):
        """Returns the current value of the current_state of the game,
        which is one of four states X_WON, O_WON, DRAW, or UNFINISHED"""
        return self._current_state


    def make_move(self, row, column, move_type):
        """Accepts a move based on row, column and type of move (x or o)
        This method checks to make sure it is a legal move and then updates
        the current_state of the game accordingly"""
        if self._current_state == "UNFINISHED":
            move_type_lower = move_type.lower()
            #The following if and elif all ensure legal input
            #and that the input is being added into an empty slot
            if move_type_lower != "x" and move_type_lower != "o":
                return False
            elif type(row) != int:
                return False
            elif type(column) != int:
                return False
            elif row < 0 or row > 2 or column < 0 or column > 2:
                return False
            elif self._board[row][column] != "":
                return False
            #The following else statement adds the desired move and then checks
            #for X_WIN, O_WIN, or DRAW
            else:
                self._board[row][column] = move_type_lower
                if self._board[0][0] == "x" and self._board[0][1] == "x" and self._board[0][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[1][0] == "x" and self._board[1][1] == "x" and self._board[1][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[2][0] == "x" and self._board[2][1] == "x" and self._board[2][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[0][0] == "x" and self._board[1][0] == "x" and self._board[2][0] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[0][1] == "x" and self._board[1][1] == "x" and self._board[2][1] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[0][2] == "x" and self._board[1][2] == "x" and self._board[2][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[0][0] == "x" and self._board[1][1] == "x" and self._board[2][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[2][0] == "x" and self._board[1][1] == "x" and self._board[0][2] == "x":
                    self._current_state = "X_WON"
                    return False
                elif self._board[0][0] == "o" and self._board[0][1] == "o" and self._board[0][2] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[1][0] == "o" and self._board[1][1] == "o" and self._board[1][2] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[2][0] == "o" and self._board[2][1] == "o" and self._board[2][2] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[0][0] == "o" and self._board[1][0] == "o" and self._board[2][0] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[0][1] == "o" and self._board[1][1] == "o" and self._board[2][1] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[0][2] == "o" and self._board[1][2] == "o" and self._board[2][2] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[0][0] == "o" and self._board[1][1] == "o" and self._board[2][2] == "o":
                    self._current_state = "O_WON"
                    return False
                elif self._board[2][0] == "o" and self._board[1][1] == "o" and self._board[0][2] == "o":
                    self._current_state = "O_WON"
                    return False
                else: #checks for a draw by looking for an empty space
                    space_full = True
                    for k in self._board:
                        for i in k:
                            if i == "":
                                space_full = False
                    if space_full == True:
                        self._current_state = "DRAW"
                        return False
            return True
        elif self._current_state != "UNFINISHED":
            return False #returns False if game is won or drawn


    def get_board(self):
        """return the board in a 3x3 fashion"""
        for item in self._board:
            print(item)


game = TicTacToe()

"""
#####Type Errors#######
#float
print(game.make_move(1.0, 0, "t"))
print(game.get_board())
print(game.get_current_state())

#column out of range (+)
print(game.make_move(4, 1.20, "o"))
print(game.get_board())
print(game.get_current_state())

#not an o or x
print(game.make_move(0, 0, "t"))
print(game.get_board())
print(game.get_current_state())

#column out of range (+)
print(game.make_move(4, 0, "o"))
print(game.get_board())
print(game.get_current_state())

#column out of range (-)
print(game.make_move(-4, 0, "o"))
print(game.get_board())
print(game.get_current_state())

#row out of range (+)
print(game.make_move(0, 4, "o"))
print(game.get_board())
print(game.get_current_state())

#row out of range (-)
print(game.make_move(0, -4, "o"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 try to fill same spot twice
print(game.make_move(0, 0, "o"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(1, 0, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(0, 0, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 0, "o"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 Give o a win horizontally and then try to keep playing
print(game.make_move(0, 0, "o"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(0, 1, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(0, 2, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 2, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 0, "x"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 Give x a win horizontally
print(game.make_move(0, 0, "x"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(0, 1, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(0, 2, "x"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 Give o a win vertically
print(game.make_move(0, 0, "o"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(1, 0, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 0, "o"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 Give o a win diagonal
print(game.make_move(0, 0, "o"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(1, 1, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 2, "o"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#######Next 4 Give x a win diagonal
print(game.make_move(0, 2, "x"))
print(game.get_board())
print(game.get_current_state())


print(game.make_move(1, 1, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 0, "x"))
print(game.get_board())
print(game.get_current_state())
"""
"""
#####next 10 will be a draw######

print(game.make_move(0, 0, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(0, 1, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(0, 2, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 0, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 1, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(1, 2, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 0, "o"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 1, "x"))
print(game.get_board())
print(game.get_current_state())

print(game.make_move(2, 2, "o"))
print(game.get_board())
print(game.get_current_state())

#draw is reached, this tries to add one
print(game.make_move(0, 2, "o"))
print(game.get_board())
print(game.get_current_state())
"""







