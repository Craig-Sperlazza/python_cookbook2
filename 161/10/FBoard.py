# project-10
# Author: Craig Sperlazza
# Date: 11/21/2019
# Description: Creates a class named FBoard that creates an instance of a
# checkers-like game where x and o to move diagonally with the goal of x
# to reach the other side of the board and for o surround
# x such that no legal moves exist.

class FBoard:
    """Class named FBoard that has three private data members: the board,
    current state of game (which will update to alert if either
    x or o have won the game or if it is unifinished), and an x piece tracker"""

    def __init__(self):
        """Initializes a board as a list made of eight list elements, tracks
         position for x, and sets the current state of the game to UNFINISHED"""
        self._board = [["", "", "", "x", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", ""],
                       ["o", "", "o", "", "o", "", "o", ""]]
        self._game_state = "UNFINISHED" #"X_WON", "O_WON", or "UNFINISHED".
        self._x_location = [0,3] #Data member to keep track of x piece.

    def get_game_state(self):
        """Method that returns the current state of the game,
        which is one of three states X_WON, O_WON, or UNFINISHED"""
        return self._game_state


    def get_x_location(self):
        """Method that returns x's current location"""
        return self._x_location


    def move_x(self, row, column):
        """Accepts a move for x based on row and column to move to.
        This method checks to make sure it is a legal move and then updates
        the state of the game accordingly"""
        if self._game_state == "UNFINISHED":
            #The following if and elif statements ensure legal input
            if type(row) != int:
                return False
            elif type(column) != int:
                return False
            elif row < 0 or row > 7 or column < 0 or column > 7: #size of board
                return False
            elif self._board[row][column] != "": #ensures space is empty
                return False
            #ensures move is diagonal
            elif row == self._x_location[0]:
                return False
            elif column == self._x_location[1]:
                return False
            # following elif Statements ensure one space only
            # row increases and column increases
            elif row > self._x_location[0] and column > self._x_location[1] and row - self._x_location[0] > 1:
                return False
            elif row > self._x_location[0] and column > self._x_location[1] and column - self._x_location[1] > 1:
                return False

            # row increases and column decreases
            elif row > self._x_location[0] and column < self._x_location[1] and row - self._x_location[0] > 1:
                return False
            elif row > self._x_location[0] and column < self._x_location[1] and self._x_location[1] - column > 1:
                return False

            # row decreases and column decreases
            elif row < self._x_location[0] and column < self._x_location[1] and self._x_location[0] - row > 1:
                return False
            elif row < self._x_location[0] and column < self._x_location[1] and self._x_location[1] - column > 1:
                return False

            # row decreases and column increases
            elif row < self._x_location[0] and column > self._x_location[1] and self._x_location[0] - row > 1:
                return False
            elif row < self._x_location[0] and column > self._x_location[1] and column - self._x_location[1] > 1:
                return False

            # The else statement adds desired move and then checks for X_WON
            else:
                self._board[row][column] = "x" #moves x to the desired space
                prior_x_position = self._x_location
                prior_x_row = self._x_location[0]
                prior_x_column = self._x_location[1]
                self._board[prior_x_row][prior_x_column] = "" #deletes prior x
                self._x_location = [row, column] #updates x data member position
                #print(self._x_location)
                #print(self._x_location[0])
                #print(self._x_location[1])
                #print(self._x_location[0]-1)

                # checks for a win by looking for an x in column 7
                if self._x_location[0] == 7:
                    self._game_state = "X_WON"
                    return True
                else:
                    return True
            #return True
        elif self._game_state != "UNFINISHED":
            return False  # returns False if game is won by x


    def move_o(self, curr_row, curr_column, desired_row, desired_column):
        """Accepts a move for o based on row/column where o currently is and
        where o desires to move. This method checks to make sure o's current
        position is accurate, that it is a legal move, and then updates
        the state of the game accordingly"""
        if self._game_state == "UNFINISHED":
        # The following if and elif all ensure legal input
        # and that the input is being added into an empty slot
            if type(curr_row) != int:
                return False
            elif type(curr_column) != int:
                return False
            elif type(desired_row) != int:
                return False
            elif type(desired_column) != int:
                return False
            elif self._board[curr_row][curr_column] != "o": #checks current pos.
                return False
            elif desired_row < 0 or desired_row > 7 or desired_column < 0 or desired_column > 7:  # size of board
                return False
            elif self._board[desired_row][desired_column] != "":  # empty space
                return False
            # ensures move is diagonal
            elif curr_row == desired_row:
                return False
            # ensures move is diagonal
            elif curr_column == desired_column:
                return False
            # Checking to see if move exceeds one space
            # row increases and column increases
            elif desired_column > curr_column and desired_column - curr_column > 1:
                return False
            # row increases and column decreases
            elif desired_column < curr_column and curr_column - desired_column > 1:
                return False
            # Ensures o only moves forward
            elif desired_row != curr_row - 1:
                return False
            else:
                self._board[desired_row][desired_column] = "o"  # o to new space
                self._board[curr_row][curr_column] = ""  # deletes prior o

                # checks for a win by o by checking available moves for x
                self.o_win_alg(self._board, self._game_state)
            return True
        elif self._game_state != "UNFINISHED":
            return False  # returns False if game is won


    def o_win_alg(self, board, state):
        """Method to check if o has won the game
        (if x has no available moves, then o wins)"""

        for nest_list in board:
            if "x" in nest_list:
                row_pos = board.index(nest_list)
                col_pos = nest_list.index("x")
                #print(row_pos, col_pos)

        if self._game_state == "UNFINISHED":
            open_tl = True
            open_tr = True
            open_bl = True
            open_br = True

            # Checking to see if moving to top left is open
            new_tl_row = row_pos - 1
            new_tl_col = col_pos - 1
            if new_tl_row < 0 or new_tl_col < 0:
                open_tl = False
            else:
                tl_board = board[row_pos - 1][col_pos - 1]
                if tl_board != "":
                    open_tl = False

            # Checking to see if moving to top right is open
            new_tr_row = row_pos - 1
            new_tr_col = col_pos + 1

            if new_tr_row < 0 or new_tr_col > 7:
                open_tr = False
            else:
                tr_board = board[row_pos - 1][col_pos + 1]
                if tr_board != "":
                    open_tr = False

            # Checking to see if moving to bottom left is open
            new_bl_row = row_pos + 1
            new_bl_col = col_pos - 1

            if new_bl_row > 7 or new_bl_col < 0:
                open_bl = False
            else:
                bl_board = board[row_pos + 1][col_pos - 1]
                if bl_board != "":
                    open_bl = False

            # Checking to see if moving to bottom right is open
            new_br_row = row_pos + 1
            new_br_col = col_pos + 1
            if new_br_row > 7 or new_br_col > 7:
                open_br = False
            else:
                br_board = board[row_pos + 1][col_pos + 1]
                if br_board != "":
                    open_br = False
            #print(open_tl, open_tr, open_bl, open_br)
            if open_tl == False and open_tr == False and open_bl == False and open_br == False:
                self._game_state = "O_WON"
                #print(current)
        return True

    def get_board(self):
        """return the board in a 8x8 grid"""
        for item in self._board:
            print(item)

fb = FBoard()

"""
#Sample test from readme
fb.move_x(1,4)
fb.move_x(2,5)
fb.move_o(7,0,6,1)
print(fb.get_game_state())
print(fb.get_board())
"""

"""
#o wins with out of bounds to left

print(fb.move_x(1, 2))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 1))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(3, 0))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())


print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 3, 5, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(5, 2, 4, 1))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(7, 0, 6, 1))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 1, 5, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(5, 2, 4, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(4, 3, 3, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(3, 2, 2, 1))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

#try o move after win
print(fb.move_o(2, 1, 1, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

#try x move after win
print(fb.move_x(2, 1))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""


"""
#o wins with x out of bounds to the right
print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 3, 5, 4))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(5, 4, 4, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(7, 6, 6, 7))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 7, 5, 6))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(3, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(4, 7))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_o(4, 5, 3, 6))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

#x tries to move after win
print(fb.move_x(3, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#o tries to move after win
print(fb.move_o(5, 6, 6, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

"""
#o wins with x out of bounds backwards
print(fb.move_o(7, 6, 6, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 5, 5, 4))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(5, 4, 4, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(4, 3, 3, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(3, 2, 2, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(2, 3, 1, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(7, 0, 6, 1))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 1, 5, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(5, 2, 4, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(4, 3, 3, 4))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(3, 4, 2, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(2, 5, 1, 4))
print(fb.get_board())
print(fb.get_game_state())

#o tries to move after win
print(fb.move_o(1, 4, 2, 5))
print(fb.get_board())
print(fb.get_game_state())
"""

"""
#o wins with x surrounded
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(3, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(4, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(5, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(6, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())


print(fb.move_o(7, 0, 6, 1))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 1, 5, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(7, 6, 6, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_o(6, 5, 5, 4))
print(fb.get_board())
print(fb.get_game_state())

#o tries to move after win
print(fb.move_o(5, 4, 4, 5))
print(fb.get_board())
print(fb.get_game_state())

#x tries to move after win
print(fb.move_x(5, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""

"""
#x wins
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(3, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(4, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(5, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(6, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_o(7, 6, 6, 7))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 4, 6, 3))
print(fb.get_board())
print(fb.get_game_state())

#x wins
print(fb.move_x(7, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#o tries to move after win
print(fb.move_o(6, 7, 5, 6))
print(fb.get_board())
print(fb.get_game_state())

#x tries to move after win
print(fb.move_x(6, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""
"""
#x can move in all directions
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(3, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(0, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""

"""
#Each o can move in all directions
print(fb.move_o(7, 6, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 5, 6))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 5, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 3, 5, 2))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 0, 6, 1))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 1, 5, 0))
print(fb.get_board())
print(fb.get_game_state())
"""

"""
#Check for moving to occupied square
#o to o
print(fb.move_o(7, 6, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

# o to x, x to o
print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 5, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(5, 4, 4, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(4, 3, 3, 2))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_x(2, 3))
print(fb.get_board())
print(fb.get_game_state())

#x and o are now in diagonal touching squares
# move x to o
#print(fb.move_x(3, 2))
#print(fb.get_board())
#print(fb.get_game_state())

#move o to x
print(fb.move_o(3, 2, 2, 3))
print(fb.get_board())
print(fb.get_game_state())

"""
"""
#X illegal moves
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(2, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())


print(fb.move_x(3, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""
"""
#backward
print(fb.move_x(2, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two backward
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#forward
print(fb.move_x(4, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two forward
print(fb.move_x(5, 4))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#left
print(fb.move_x(3, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two left
print(fb.move_x(3, 2))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#right
print(fb.move_x(3, 5))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two right
print(fb.move_x(3, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two l diag
print(fb.move_x(5, 2))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two r diag
print(fb.move_x(5, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two backleft diag
print(fb.move_x(1, 2))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#two backright diag
print(fb.move_x(1, 6))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#random space
print(fb.move_x(5, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

#out of bounds
print(fb.move_x(-2, 3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())

print(fb.move_x(4, -3))
print(fb.get_board())
print(fb.get_game_state())
print(fb.get_x_location())
"""


"""
#o illegal moves
#forward
print(fb.move_o(7, 2, 6, 2))
print(fb.get_board())
print(fb.get_game_state())

#backward
print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 7, 5))
print(fb.get_board())
print(fb.get_game_state())

#left
print(fb.move_o(7, 0, 6, 1))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 1, 6, 0))
print(fb.get_board())
print(fb.get_game_state())

#right
print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 3, 6, 4))
print(fb.get_board())
print(fb.get_game_state())

#back diagonal left
print(fb.move_o(6, 3, 7, 2))
print(fb.get_board())
print(fb.get_game_state())

#back diagonal right
print(fb.move_o(6, 3, 7, 4))
print(fb.get_board())
print(fb.get_game_state())
"""

"""
#o illegal moves two spaces

#two spaces back left diagonal
print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 5, 6))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(5, 6, 7, 4))
print(fb.get_board())
print(fb.get_game_state())

#two spaces back right diagonal
print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 5, 5, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(5, 4, 4, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(4, 3, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

#O wrong starting coordinates
print(fb.move_o(7, 4, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 4, 5, 3))
print(fb.get_board())
print(fb.get_game_state())

#o out of bounds moves
print(fb.move_o(7, 2, -3, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 2, 6, -4))
print(fb.get_board())
print(fb.get_game_state())

#o out of bounds moves
print(fb.move_o(7, 2, -3, -4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(7, 2, -6, -4))
print(fb.get_board())
print(fb.get_game_state())
"""


"""
#two spaces right diag
print(fb.move_o(7, 4, 5, 6))
print(fb.get_board())
print(fb.get_game_state())

#two spaces left diag
print(fb.move_o(7, 2, 5, 0))
print(fb.get_board())
print(fb.get_game_state())

#two spaces forward
print(fb.move_o(7, 6, 5, 6))
print(fb.get_board())
print(fb.get_game_state())

#two spaces backwards
print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 3, 5, 4))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(5, 4, 4, 5))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(4, 5, 6, 5))
print(fb.get_board())
print(fb.get_game_state())

#two space left
print(fb.move_o(7, 2, 6, 3))
print(fb.get_board())
print(fb.get_game_state())

print(fb.move_o(6, 3, 6, 1))
print(fb.get_board())
print(fb.get_game_state())

#two spaces right
print(fb.move_o(6, 3, 6, 5))
print(fb.get_board())
print(fb.get_game_state())
"""

#Initial Testing
"""
print(fb.move_x(1, 4))
print(fb.get_board())
print(fb.get_game_state())


print(fb.move_x(2, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_x(3, 6))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_x(4, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_x(5, 6))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())

print(fb.move_x(6, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

"""
o tries two rows
print(fb.move_o(6, 3, 4, 2))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""


"""o tries two column 
print(fb.move_o(6, 3, 4, 5))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

"""o tries forward
print(fb.move_o(6, 3, 5, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

"""o tries backwards
print(fb.move_o(5, 4, 6, 3))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

""" x wins
print(fb.move_x(7, 4))
print(fb.get_board())
print(fb.get_game_state())
#print(fb.get_x_location())
"""

"""tests diagonal
print(fb.move_x(3, 5))
print(fb.get_board())
print(fb.get_x_location())
"""


