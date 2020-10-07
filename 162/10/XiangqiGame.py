
# Portfolio Project
# Author: Craig Sperlazza
# Date: 2/26/2020
# Description: Creates a game of Xiangi, also know as Chinese chess. This game
#   will be set up primarily through the XiangqiGame class and will use pieces
#   created in a Piece Class and various sub-classes (one for each piece type)
#   that inherits through the Piece class.


class XiangqiGame:
    """Class named XiangiGame which initializes the Game and Board.
    Data Members:
        The board which is initialized as a list with 10 nested lists and
            each nested list is initialized as 9 empty strings.
            This creates the 10x9 board
        A move data member. This will track whose turn it is (red or black)
        A game state data member initialized to UNFINISHED and the possible
            states of RED_WON, BLACK_WON, or UNFINISHED"
        A data member named is_in_check which is set to False
            and updated if the King is in check.
        A count data member initialized to one.
            This will be used to keep track of the count of moves.
    Methods:
        Get and set methods for each of the data members
        The Game class also calls the subclasses to initialize
            each piece object into the board.
        Convert coordinates method:
            This will take the string coordinates given and convert them to
            integers to use as list coordinates.
        Print board method: prints the board in readable format.
        It also has an in check method that will determine if a given move
        is invalid due to placing the king in check or if it is a valid move,
        it will check if the other side is in check

        Make move method
            Takes a current location and next location as parameter
            Converts this to integers to use as list coordinates
            Validate that it is a legal move
            Check that the position has a piece
            That if it is red’s turn, red is moving a red piece, etc.
            Then it will call a method in the piece subclass to
                make sure that is a valid move for the piece
            If that returns True
                It will then call various helper methods within the Game class
                to further analyze if that is a legal move
            If all of these returns True
                It will then call a final method to make the move which
                will update the board with the piece in the new position
                and update the old position to empty. It will also change
                game state if necessary and update turn and count. """

    def __init__(self):
        """Initializes a board as a list made of ten list elements, all of
        which are initially set as an empty string.
        The init function also creates and sets the current state of the game to
        UNFINISHED, sets the initial move to red and sets in_check to False"""
        self._board = [["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],
                       ["", "", "", "", "", "", "", "", ""],]
        self._red_move = True
        self._game_state = "UNFINISHED"
        self._is_in_check = False

        ############  INITIALIZE PIECES AND PLACE ON BOARD     #################
        ########################################################################
        ####################   RED PIECES  #####################################
        ########################################################################

        ####################   RED ROOKS   #####################################
        red_rook1 = Rook('RR', 'red', 'rook', 'a1')
        str_coord = 'a1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook1 #have to do y first because nested list

        red_rook2 = Rook('RR', 'red', 'rook', 'i1')
        str_coord = 'i1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_rook2  #have to do y first because nested list

        ####################   RED KNIGHTS/HORSES  #############################
        red_knight1 = Knight('RN', 'red', 'knight', 'b1')
        str_coord = 'b1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight1  #have to do y first because nested list

        red_knight2 = Knight('RN', 'red', 'knight', 'h1')
        str_coord = 'h1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_knight2  #have to do y first because nested list

        ####################   RED BISHOPS/ELEPHANTS  ##########################
        red_bishop1 = Bishop('RB', 'red', 'bishop', 'c1')
        str_coord = 'c1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop1  #have to do y first because nested list

        red_bishop2 = Bishop('RB', 'red', 'bishop', 'g1')
        str_coord = 'g1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_bishop2  #have to do y first because nested list

        ####################   RED GUARDS   ####################################
        red_guard1 = Guard('RG', 'red', 'guard', 'd1')
        str_coord = 'd1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard1  # have to do y first because nested list

        red_guard2 = Guard('RG', 'red', 'guard', 'f1')
        str_coord = 'f1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_guard2  # have to do y first because nested list

        ####################   RED KING    #####################################
        red_king = King('RK', 'red', 'king', 'e1')
        str_coord = 'e1'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_king  # have to do y first because nested list


        ####################   RED CANNONS   ###################################
        red_cannon1 = Cannon('RC', 'red', 'cannon', 'b3')
        str_coord = 'b3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_cannon1  #have to do y first because nested list

        red_cannon2 = Cannon('RC', 'red', 'cannon', 'h3')
        str_coord = 'h3'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_cannon2  #have to do y first because nested list

        ####################   RED PAWNS   #####################################
        red_pawn1 = Pawn('RP', 'red', 'pawn', 'a4')
        str_coord = 'a4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn1  # have to do y first because nested list

        red_pawn2 = Pawn('RP', 'red', 'pawn', 'c4')
        str_coord = 'c4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn2  # have to do y first because nested list

        red_pawn3 = Pawn('RP', 'red', 'pawn', 'e4')
        str_coord = 'e4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn3  # have to do y first because nested list

        red_pawn4 = Pawn('RP', 'red', 'pawn', 'g4')
        str_coord = 'g4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn4  # have to do y first because nested list

        red_pawn5 = Pawn('RP', 'red', 'pawn', 'i4')
        str_coord = 'i4'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = red_pawn5  # have to do y first because nested list

        ########################################################################
        ####################   BLACK PIECES  ###################################
        ########################################################################

        ####################   BLACK ROOKS   ###################################
        black_rook1 = Rook('BR', 'black', 'rook', 'a10')
        str_coord = 'a10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook1  #have to do y first because nested list

        black_rook2 = Rook('BR', 'black', 'rook', 'i10')
        str_coord = 'i10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_rook2  #have to do y first because nested list

        ####################   BLACK KNIGHTS/HORSES  ###########################
        black_knight1 = Knight('BN', 'black', 'knight', 'b10')
        str_coord = 'b10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight1  #have to do y first--nested list

        black_knight2 = Knight('BN', 'black', 'knight', 'h10')
        str_coord = 'h10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_knight2  # have to do y first--nested list

        ####################   BLACK BISHOPS/ELEPHANTS  ########################
        black_bishop1 = Bishop('BB', 'black', 'bishop', 'c10')
        str_coord = 'c10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop1  # have to do y first--nested list

        black_bishop2 = Bishop('BB', 'black', 'bishop', 'g10')
        str_coord = 'g10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_bishop2  # have to do y first--nested list

        ####################   BLACK GUARDS   ##################################
        black_guard1 = Guard('BG', 'black', 'guard', 'd10')
        str_coord = 'd10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard1  # have to do y first--nested list

        black_guard2 = Guard('BG', 'black', 'guard', 'f10')
        str_coord = 'f10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_guard2  # have to do y first--nested list

        ####################   BLACK KING    ###################################
        black_king = King('BK', 'black', 'king', 'e10')
        str_coord = 'e10'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_king  # have to do y first because nested list

        ####################   BLACK CANNONS   #################################
        black_cannon1 = Cannon('BC', 'black', 'cannon', 'b8')
        str_coord = 'b8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_cannon1  # have to do y first--nested list

        black_cannon2 = Cannon('BC', 'black', 'cannon', 'h8')
        str_coord = 'h8'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_cannon2  # have to do y first--nested list

        ####################   BLACK PAWNS   ##################################
        black_pawn1 = Pawn('BP', 'black', 'pawn', 'a7')
        str_coord = 'a7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn1  # have to do y first--nested list

        black_pawn2 = Pawn('BP', 'black', 'pawn', 'c7')
        str_coord = 'c7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn2  # have to do y first--nested list

        black_pawn3 = Pawn('BP', 'black', 'pawn', 'e7')
        str_coord = 'e7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn3  # have to do y first--nested list

        black_pawn4 = Pawn('BP', 'black', 'pawn', 'g7')
        str_coord = 'g7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn4  # have to do y first--nested list

        black_pawn5 = Pawn('BP', 'black', 'pawn', 'i7')
        str_coord = 'i7'
        list_coord = self.convert_coord(str_coord)
        x = list_coord[0]
        y = list_coord[1]
        self._board[y][x] = black_pawn5  # have to do y first--nested list

    def get_game_state(self):
        """Method that returns the current state of the game,
        which is one of three states RED_WON, BLACK_WON, or UNFINISHED"""
        return self._game_state

    def set_game_state(self, color):
        """Method that sets the current state of the game,
        which is one of three states RED_WON, BLACK_WON, or UNFINISHED"""
        if color == "BLACK":
            self._game_state = "BLACK_WON"
        elif color == "RED":
            self._game_state = "RED_WON"

    def get_red_move(self):
        """Method that returns True if it is Red's move"""
        return self._red_move

    def set_red_move(self):
        """Method to set whether it is red's move (True) or blacks
        This will be called after every successful move"""
        if self._red_move == True:
            self._red_move = False
        else:
            self._red_move = True

    def convert_coord(self, str_pos):
        """
        Method to convert string move to a list of integer coordinates on board.
        param: string value representing 'xy' coordinates
        returns: list of integers [x, y] coordinates
        """
        x = 0
        y = 0

        if str_pos[0] == 'a':
            x = 0
        elif str_pos[0] == 'b':
            x = 1
        elif str_pos[0] == 'c':
            x = 2
        elif str_pos[0] == 'd':
            x = 3
        elif str_pos[0] == 'e':
            x = 4
        elif str_pos[0] == 'f':
            x = 5
        elif str_pos[0] == 'g':
            x = 6
        elif str_pos[0] == 'h':
            x = 7
        elif str_pos[0] == 'i':
            x = 8

        if str_pos[1] == '1' and len(str_pos) == 3:
            y = 0
            #elif len(str_pos)< 2:
        elif str_pos[1] == '1' and len(str_pos) < 3:
            y = 9
        elif str_pos[1] == '2':
            y = 8
        elif str_pos[1] == '3':
            y = 7
        elif str_pos[1] == '4':
            y = 6
        elif str_pos[1] == '5':
            y = 5
        elif str_pos[1] == '6':
            y = 4
        elif str_pos[1] == '7':
            y = 3
        elif str_pos[1] == '8':
            y = 2
        elif str_pos[1] == '9':
            y = 1
        return [x, y]
        # new = [x, y]
        # print(new)

    def get_board(self):
        """return the board in list form in its current position"""
        return self._board

    def set_board(self, x, y, x1, y1, piece):
        """Updates the board once a move has been validated as legal
        this will put the piece in the end spot and return the original spot
        to an empty string"""
        self._board[y1][x1] = piece
        self._board[y][x] = ""

    def set_board_reverse(self, x, y, x1, y1, start_piece, end_piece):
        """Reverses the board if an otherwise legal move would have put the
        moving color's king in check. This will put the  original starting piece
        and the original ending piece back into their original positions
        This is used for when a piece moves into check and must be reversed
         to the original position"""
        self._board[y1][x1] = end_piece
        self._board[y][x] = start_piece

    def print_board(self):
        """return the board in a 9x10 grid"""
        x = 10
        for item in self._board:
            # print(x)
            print(x, item)
            x -= 1
        print("   A   B   C   D   E   F   G   H   I")

    def color_check(self, start, end):
        """This method ensures that the player is not trying to move a
        piece of one color to a spot that has the same color piece"""
        if end == "":
            #print("OK")
            return
        elif start.get_color() == end.get_color():
            #print("same color")
            return False
        else:
            return

    def special_move_check(self, x, y, x2, y2, start, end):
        """ input: start(x, y), end(x2, y2), start piece, end piece
        This is the function that will check to see if the knight cannon
        special move is being called. IF it passes all the requirements
        (see comments below)
        it will return True and the main code will call the engage_special_move
        method to actually perform the swap"""
        #check that there is a piece there
        if start == "":
            #print("istart")
            return False
        elif end == "":
            #print("iend")
            return False
        #check that they are both the same color
        elif start.get_color() != end.get_color():
            #print("Icolor")
            return False
        #check that one is a cannon and one is a knight
        elif start.get_type() != "cannon" and start.get_type() != "knight":
            #print("istartpiece")
            return False
        elif end.get_type() != "cannon" and end.get_type() != "knight":
            #print("iendpiece")
            return False

        ####RED SIDE####
        #left side, red
        elif x == 1 and y == 9 and x2 == 1 and y2 == 7:
            return True
        elif x == 1 and y == 7 and x2 == 1 and y2 == 9:
            return True
        #right side red
        elif x == 7 and y == 9 and x2 == 7 and y2 == 7:
            return True
        elif x == 7 and y == 7 and x2 == 7 and y2 == 9:
            return True

        #left knight to right, red
        elif x == 1 and y == 9 and x2 == 7 and y2 == 7:
            return True
        elif x == 7 and y == 7 and x2 == 1 and y2 == 9:
            return True

        # right knight to left, red
        elif x == 7 and y == 9 and x2 == 1 and y2 == 7:
            return True
        elif x == 1 and y == 7 and x2 == 7 and y2 == 9:
            return True

        ####BLACK SIDE####
        # left side, black
        elif x == 1 and y == 0 and x2 == 1 and y2 == 2:
            return True
        elif x == 1 and y == 2 and x2 == 1 and y2 == 0:
            return True
        # right side black
        elif x == 7 and y == 0 and x2 == 7 and y2 == 2:
            return True
        elif x == 7 and y == 2 and x2 == 7 and y2 == 0:
            return True

        # left knight to right, black
        elif x == 1 and y == 0 and x2 == 7 and y2 == 2:
            return True
        elif x == 7 and y == 2 and x2 == 1 and y2 == 0:
            return True

        # right knight to left, black
        elif x == 7 and y == 0 and x2 == 1 and y2 == 2:
            return True
        elif x == 1 and y == 2 and x2 == 7 and y2 == 0:
            return True

    def engage_special_move(self, x, y, x2, y2, start, end):
        """performs the knight cannon swap if it has been validated by the
        special move check. This is slightly different from the normal move
        because it is swapping the pieces, not eliminating the end piece"""
        self._board[y2][x2] = start
        self._board[y][x] = end

    def special_bishop_move(self, x1, y1, x2, y2, piece):
        """
        Helper function for the make-move method. This method:
        Checks to ensure there is no intervening piece blocking the bishops
        desired move
        :return False if move rule is violated"""
        #TOP LEFT
        if x2 == (x1 - 2) and y2 == (y1 - 2):
            #print("TL")
            int_piece = self._board[y1-1][x1-1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do itTL")
                return False
            else:
                #print("empty good to goTL")
                return
        #Bishop is trying to move to the TOP RIGHT diagonal
        elif x2 == (x1 + 2) and y2 == (y1 - 2):
            #print("TR")
            int_piece = self._board[y1 - 1][x1 + 1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do itTR")
                return False
            else:
                #print("empty good to goTR")
                return
        #BOTTOM LEFT
        elif x2 == (x1 - 2) and y2 == (y1 + 2):
            #print("BL")
            int_piece = self._board[y1 + 1][x1 - 1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do itBL")
                return False
            else:
                #print("empty good to goBL")
                return
        #BOTTOM RIGHT
        elif x2 == (x1 + 2) and y2 == (y1 + 2):
            #print("BR")
            int_piece = self._board[y1 + 1][x1 + 1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do itBR")
                return False
            else:
                #print("empty good to goBR")
                return
        else:
            return False

    def special_knight_move(self, x1, y1, x2, y2, piece):
        """
        Helper function for the make-move method. This method:
        Checks to ensure there is no intervening piece blocking the knights
        desired move
        :return False if move rule is violated"""
        #TOP LEFT (Top left and top right depend on same intevening piece)
        if x2 == (x1 - 1) and y2 == (y1 - 2):
            int_piece = self._board[y1 - 1][x1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it UL")
                return False
            else:
                #print("empty good to go UL")
                return
        #Top Right
        elif x2 == (x1 + 1) and y2 == (y1 - 2):
            int_piece = self._board[y1 - 1][x1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it UR")
                return False
            else:
                #print("empty good to go UR")
                return
        #Right up and right down depend on same piece
        #right up
        elif x2 == (x1 + 2) and y2 == (y1 - 1):
            int_piece = self._board[y1][x1+1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it RU")
                return False
            else:
                #print("empty good to go RU")
                return
        elif x2 == (x1 + 2) and y2 == (y1 + 1):
            int_piece = self._board[y1][x1 + 1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it RD")
                return False
            else:
                #print("empty good to go RD")
                return
        ###########################
        # down right and down left depend on same piece
        # down right
        elif x2 == (x1 + 1) and y2 == (y1 + 2):
            int_piece = self._board[y1+1][x1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it DR")
                return False
            else:
                #print("empty good to go DR")
                return
        #down left
        elif x2 == (x1 - 1) and y2 == (y1 + 2):
            int_piece = self._board[y1 + 1][x1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it DR")
                return False
            else:
                #print("empty good to go DR")
                return
        #Left down and left up both depend on same piece
        #left down
        elif x2 == (x1 - 2) and y2 == (y1 + 1):
            int_piece = self._board[y1][x1-1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it LD")
                return False
            else:
                #print("empty good to go LD")
                return
        #left up
        elif x2 == (x1 - 2) and y2 == (y1 - 1):
            int_piece = self._board[y1][x1 - 1]
            #print(int_piece, "piece")
            if int_piece != "":
                #print("piece there cant do it LD")
                return False
            else:
                #print("empty good to go LD")
                return
        else:
            return

    def special_rook_move(self, x1, y1, x2, y2, piece):
        """
        helper function for the make-move method. This method:
        Checks to ensure there is no intervening piece blocking the rooks
        desired move
        :return False if move rule is violated"""
        #moving down the board (y is increasing)
        if x2 == x1 and y2 > y1:
            spaces = (y2 - y1) #- 1 #Spaces to check between y1 and y2
            coord_y = y1 + 1 #will start at the next coordinate from start
            for i in range(1, spaces):
                int_piece = self._board[coord_y][x1]
                #print(int_piece, "piece")
                if int_piece != "":
                    #print("piece there cant do it")
                    return False
                else:
                    #print("empty good to go for this square", coord_y)
                    coord_y += 1
            return

        # moving right across the board (x is increasing)
        if x2 > x1 and y2 == y1:
            spaces = (x2 - x1)  #Spaces to check between x1 and x2
            coord_x = x1 + 1  # will start at the next coordinate from start
            for i in range(1, spaces):
                int_piece = self._board[y1][coord_x]
                #print(int_piece, "piece")
                if int_piece != "":
                    #print("piece there cant do it")
                    return False
                else:
                    #print("empty good to go for this square", coord_x)
                    coord_x += 1
            return

        # moving left across the board (x is decreasing)
        if x2 < x1 and y2 == y1:
            spaces = (x1 - x2)  # Spaces to check between x1 and x2
            coord_x = x1 - 1  # will start at the next coordinate from start
            for i in range(1, spaces):
                int_piece = self._board[y1][coord_x]
                #print(int_piece, "piece")
                if int_piece != "":
                    #print("piece there cant do it")
                    return False
                else:
                    #print("empty good to go for this square", coord_x)
                    coord_x -= 1
            return

        # moving up the board (y is decreasing)
        if x2 == x1 and y2 < y1:
            spaces = (y1 - y2)  # Spaces to check between y1 and y2
            coord_y = y1 - 1  # will start at the next coordinate from start
            for i in range(1, spaces):
                int_piece = self._board[coord_y][x1]
                #print(int_piece, "piece")
                if int_piece != "":
                    #print("piece there cant do it")
                    return False
                else:
                    #print("empty good to go for this square", coord_y)
                    coord_y -= 1
            return


    def special_king_move(self, x1, y1, x2, y2, piece):
        """
        Helper function for the make-move method. This method:
        Checks to ensure that the two generals will never face each other.
        That means that this function will check the piece being moved on the
        x coordinates and make sure there is at least one intervening piece
        between the two kings if that piece is moving off the x file it is
        starting on
        :return False if move rule is violated"""

        if x2 != x1:
            if x1 == 3 or x1 == 4 or x1 == 5:
                #print("test x1 y1 x2", x1, y1, x2)
                #y decreasing side of board----BLACK KING
                spaces_dec = (y1 - 0) + 1 #Spaces to check between y1 row 0
                coord_y_dec = y1 - 1 #will start at next coordinate from start
                black_king_open = False
                for i in range(1, spaces_dec):
                    if y1 == 0 or y1 == 9:
                        break
                    else:
                        int_piece = self._board[coord_y_dec][x1]
                    #print(int_piece, "decpiece")
                    if int_piece == "":
                        coord_y_dec -= 1
                    else:
                        if int_piece.get_type() == "king":
                            #print(int_piece.get_type(), "black king")
                            black_king_open = True
                            break
                        else:
                            #print(int_piece.get_type(), "other piece")
                            black_king_open = False
                            break

                #y increasing side of board---RED KING
                spaces_inc = (9 - y1) + 1  # Spaces to check between y1 row 0
                coord_y_inc = y1 + 1  # will start at next coordinate from start
                red_king_open = False
                for i in range(1, spaces_inc):
                    if y1 == 9 or y1 == 0:
                        #int_piece = self._board[y1][x1]
                        break
                    else:
                        int_piece = self._board[coord_y_inc][x1]
                    #print(int_piece, "incpiece")
                    if int_piece == "":
                        coord_y_inc += 1
                    else:
                        #print(int_piece)
                        if int_piece.get_type() == "king":
                            #print(int_piece.get_type(), "red king")
                            red_king_open = True
                            break
                        else:
                            #print(int_piece.get_type(), "Other Type of Piece")
                            red_king_open = False
                            break
                if red_king_open == True and black_king_open == True:
                    return False
                else:
                    return
            else:
                return
        else:
            return

    def special_cannon_move(self, x1, y1, x2, y2, piece):
        """Helper Function for make_move. Checks to ensure there is
        no intervening piece blocking the cannons desired move,
        unless the cannon is taking, which should have exactly
        one intervening piece
        :return: False if the move rules are violated"""
        end_piece = self._board[y2][x2]
        piece_count = 0 #number of pieces between start and end

        if end_piece == "":     #should be no intervening pieces
            #moving down the board (y is increasing)
            if x2 == x1 and y2 > y1:
                spaces = (y2 - y1) #- 1 #Spaces to check between y1 and y2
                coord_y = y1 + 1 #will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[coord_y][x1]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        #print("piece there cant do it")
                        return False
                    else:
                        #print("empty good to go for this square", coord_y)
                        coord_y += 1
                return

            # moving right across the board (x is increasing)
            if x2 > x1 and y2 == y1:
                spaces = (x2 - x1)  #Spaces to check between x1 and x2
                coord_x = x1 + 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[y1][coord_x]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        #print("piece there cant do it")
                        return False
                    else:
                        #print("empty good to go for this square", coord_x)
                        coord_x += 1
                return

            # moving left across the board (x is decreasing)
            if x2 < x1 and y2 == y1:
                spaces = (x1 - x2)  # Spaces to check between x1 and x2
                coord_x = x1 - 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[y1][coord_x]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        #print("piece there cant do it")
                        return False
                    else:
                        #print("empty good to go for this square", coord_x)
                        coord_x -= 1
                return

            # moving up the board (y is decreasing)
            if x2 == x1 and y2 < y1:
                spaces = (y1 - y2)  # Spaces to check between y1 and y2
                coord_y = y1 - 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[coord_y][x1]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        #print("piece there cant do it")
                        return False
                    else:
                        #print("empty good to go for this square", coord_y)
                        coord_y -= 1
                return

        elif end_piece != "":
            # have a piece at end, so need exactly one intervening piece
            # moving down the board (y is increasing)
            if x2 == x1 and y2 > y1:
                spaces = (y2 - y1)  # - 1 #Spaces to check between y1 and y2
                coord_y = y1 + 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[coord_y][x1]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        piece_count += 1
                        coord_y += 1
                        #print("piece, piece count = ", piece_count)
                    else:
                        #print("empty square, piece count", piece_count)
                        coord_y += 1
                if piece_count != 1:
                    #print(piece_count, "False")
                    return False
                else:
                    #print(piece_count, "True")
                    return

            # moving right across the board (x is increasing)
            if x2 > x1 and y2 == y1:
                spaces = (x2 - x1)  # Spaces to check between x1 and x2
                coord_x = x1 + 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[y1][coord_x]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        piece_count += 1
                        coord_x += 1
                        #print("piece, piece count = ", piece_count)
                    else:
                        #print("empty square, piece count", piece_count)
                        coord_x += 1
                if piece_count != 1:
                    #print(piece_count, "False")
                    return False
                else:
                    #print(piece_count, "True")
                    return

            # moving left across the board (x is decreasing)
            if x2 < x1 and y2 == y1:
                spaces = (x1 - x2)  # Spaces to check between x1 and x2
                coord_x = x1 - 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[y1][coord_x]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        piece_count += 1
                        coord_x -= 1
                        #print("piece, piece count = ", piece_count)
                    else:
                        #print("empty square, piece count", piece_count)
                        coord_x -= 1
                if piece_count != 1:
                    #print(piece_count, "False")
                    return False
                else:
                    #print(piece_count, "True")
                    return

            # moving up the board (y is decreasing)
            if x2 == x1 and y2 < y1:
                spaces = (y1 - y2)  # Spaces to check between y1 and y2
                coord_y = y1 - 1  # will start at the next coordinate from start
                for i in range(1, spaces):
                    int_piece = self._board[coord_y][x1]
                    #print(int_piece, "piece")
                    if int_piece != "":
                        piece_count += 1
                        coord_y -= 1
                        #print("piece, piece count = ", piece_count)
                    else:
                        #print("empty good to go for this square", coord_y)
                        coord_y -= 1
                if piece_count != 1:
                    #print(piece_count, "False")
                    return False
                else:
                    #print(piece_count, "True")
                    return

    def make_move(self, begin_coord, end_coord):
        """
        :param begin_coord: This will be a string representation of a coordinate
        move using algebraic notation. This will be the position of the piece
        the player wishes to move
        :param end_coord: This will be a string representation of a coordinate
        move using algebraic notation. This will be the position the player
        wishes to move to
        :Helper: This function calls numerous helper functions. Each is called
        below together with detailed comments as to what that helper function
        will do
        :return:
        If the game has been won, it will Return False
        If there is no piece at the coordinates, it will return False
        If Red tries to move Black (and vice versa), it will return False
        If the desired move is illegal for that piece type, it will return False
        If the desired move violates a principal of the game, such as generals
        facing each other or move into check, it will return False
        Otherwise, it will
            make the move by updating the board
            update game state if applicable
            update players turn
            and Return True
        """
        begin_coord = begin_coord
        end_coord = end_coord
        begin_coord_lst = self.convert_coord(begin_coord)
        end_coord_lst = self.convert_coord(end_coord)
        x = begin_coord_lst[0]
        y = begin_coord_lst[1]
        x_end = end_coord_lst[0]
        y_end = end_coord_lst[1]

        piece = self._board[y][x]
        end_spot = self._board[y_end][x_end]

        #print(piece.get_color())
        #print(piece.get_name())
        #print(piece.get_type())
        #print(piece.get_read())

        if self._game_state == "UNFINISHED":
            #no piece on the coordinates
            if piece == "":
                #print(False)
                return False

            #no actual movement
            if x == x_end and y == y_end:
                return False

            #black is trying to move a red piece
            if piece.get_color() == "red" and self._red_move == False:
                #print("wrongcolor--black cant move red")
                return False
            # red is trying to move a black piece
            elif piece.get_color() == "black" and self._red_move == True:
                #print("wrongcolor--red cant move black")
                return False


            # special elephant cannon exchange move
            #have to run this before the color check below
            special_move = self.special_move_check(x, y, x_end, y_end, piece, end_spot)
            if special_move == False:
                throwaway2 = 3
                #print("elephantCannon exchange FALSE")
                #pass
            else:
                #print("elephantCannon exchange Engaged")
                self.engage_special_move(x, y, x_end, y_end, piece, end_spot)
                self.set_red_move()
                return True

            #This will return False if the end coordinate is the same color as
            #the piece. It will call the color_check function defined in this
            #Game class
            same_color = self.color_check(piece, end_spot)
            if same_color == False:
                return False

            #This will ensure that the two kings will not face each other
            special_king = self.special_king_move(x, y, x_end, y_end, piece)
            if special_king == False:
                #print("Two Kings cant face each other FALSE")
                return False
            else:
                pass

            if piece.get_type() == "rook":
                valid = piece.rook_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # Call this function to ensure there is no intervening piece
                    special_rook = self.special_rook_move(x, y, x_end, y_end, piece)
                    if special_rook == False:
                        #print("coming back false")
                        return False
                    else:
                        #print("rook coming back valid")
                        prev_start = self._board[y][x] #save previous start
                        prev_end = self._board[y_end][x_end] #save previous end
                        self.set_board(x, y, x_end, y_end, piece) #execute move

                        if self._red_move == True:
                            color = "red"
                        else:
                            color = "black"

                        #now we need to check and see if the move moved the
                        # player into check so we will update the board (above)
                        # and then check to see if that color is in check 
                        # so if black moved, we check to see whether black is in
                        # check as if it is red's next move.
                        # If black moved into check, we will reverse the move

                        in_check = self.is_in_check(color)
                        if in_check == True:
                            #print("can't move into check")
                            self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                            #print("board should be reversed")
                            return False
                        else:
                            #updates the color
                            self.set_red_move()
                            return True


            elif piece.get_type() == "pawn":
                valid = piece.pawn_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    #print("pawn coming back valid")
                    prev_start = self._board[y][x]  #save previous piece start
                    prev_end = self._board[y_end][x_end]  #save previous end
                    self.set_board(x, y, x_end, y_end, piece)  #execute move

                    if self._red_move == True:
                        color = "red"
                    else:
                        color = "black"

                    # now we need to check and see if the move moved the
                    # player into check so we will update the board (above)
                    # and then check to see if that color is in check
                    # so if black moved, we check to see whether black is in
                    # check as if it is red's next move.
                    # If black moved into check, we will reverse the move

                    in_check = self.is_in_check(color)
                    if in_check == True:
                        #print("can't move into check")
                        self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                        #print("board should be reversed")
                        return False
                    else:
                        # updates the color
                        self.set_red_move()
                        return True

            elif piece.get_type() == "cannon":
                valid = piece.cannon_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # Call this function to ensure there is no intervening piece
                    special_cannon = self.special_cannon_move(x, y, x_end, y_end, piece)
                    if special_cannon == False:
                        #print("coming back false")
                        return False
                    else:
                        # print("cannon coming back valid")
                        prev_start = self._board[y][x]  #save previous start
                        prev_end = self._board[y_end][x_end]  #save previous end
                        self.set_board(x, y, x_end, y_end, piece)  #execute move

                        if self._red_move == True:
                            color = "red"
                        else:
                            color = "black"

                        # now we need to check and see if the move moved the
                        # player into check so we will update the board (above)
                        # and then check to see if that color is in check
                        # so if black moved, we check to see whether black is in
                        # check as if it is red's next move.
                        # If black moved into check, we will reverse the move

                        in_check = self.is_in_check(color)
                        if in_check == True:
                            # print("can't move into check")
                            self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                            # print("board should be reversed")
                            return False
                        else:
                            # updates the color
                            self.set_red_move()
                            return True

            elif piece.get_type() == "king":
                valid = piece.king_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # print("king coming back valid")
                    prev_start = self._board[y][x]  # save previous piece start
                    prev_end = self._board[y_end][x_end]  # save previous end
                    self.set_board(x, y, x_end, y_end, piece)  # execute move

                    if self._red_move == True:
                        color = "red"
                    else:
                        color = "black"

                    # now we need to check and see if the move moved the
                    # player into check so we will update the board (above)
                    # and then check to see if that color is in check
                    # so if black moved, we check to see whether black is in
                    # check as if it is red's next move.
                    # If black moved into check, we will reverse the move

                    in_check = self.is_in_check(color)
                    if in_check == True:
                        # print("can't move into check")
                        self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                        # print("board should be reversed")
                        return False
                    else:
                        # updates the color
                        self.set_red_move()
                        return True

            elif piece.get_type() == "bishop":
                valid = piece.bishop_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # print(piece.get_color(), "bishop valid move")
                    #Call this function to ensure there is no intervening piece
                    special_bishop = self.special_bishop_move(x, y, x_end, y_end, piece)
                    if special_bishop == False:
                        #print("coming back false")
                        return False
                    else:
                        # print("bishop coming back valid")
                        prev_start = self._board[y][x]  #save previous start
                        prev_end = self._board[y_end][x_end]  #save previous end
                        self.set_board(x, y, x_end, y_end, piece)  #execute move

                        if self._red_move == True:
                            color = "red"
                        else:
                            color = "black"

                        # now we need to check and see if the move moved the
                        # player into check so we will update the board (above)
                        # and then check to see if that color is in check
                        # so if black moved, we check to see whether black is in
                        # check as if it is red's next move.
                        # If black moved into check, we will reverse the move

                        in_check = self.is_in_check(color)
                        if in_check == True:
                            # print("can't move into check")
                            self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                            # print("board should be reversed")
                            return False
                        else:
                            # updates the color
                            self.set_red_move()
                            return True

            elif piece.get_type() == "guard":
                valid = piece.guard_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # print("guard coming back valid")
                    prev_start = self._board[y][x]  #save the previous start
                    prev_end = self._board[y_end][x_end]  #save previous end
                    self.set_board(x, y, x_end, y_end, piece)  #execute move

                    if self._red_move == True:
                        color = "red"
                    else:
                        color = "black"

                    # now we need to check and see if the move moved the
                    # player into check so we will update the board (above)
                    # and then check to see if that color is in check
                    # so if black moved, we check to see whether black is in
                    # check as if it is red's next move.
                    # If black moved into check, we will reverse the move

                    in_check = self.is_in_check(color)
                    if in_check == True:
                        # print("can't move into check")
                        self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                        # print("board should be reversed")
                        return False
                    else:
                        # updates the color
                        self.set_red_move()
                        return True

            elif piece.get_type() == "knight":
                valid = piece.knight_valid_move(x, y, x_end, y_end, piece)
                if valid == False:
                    return False
                else:
                    # Call this function to ensure there is no intervening piece
                    special_knight = self.special_knight_move(x, y, x_end, y_end, piece)
                    if special_knight == False:
                        #print("coming back false")
                        return False
                    else:
                        # print("rook coming back valid")
                        prev_start = self._board[y][x]  #save previous start
                        prev_end = self._board[y_end][x_end]  #save prev. end
                        self.set_board(x, y, x_end, y_end, piece)  #execute move

                        if self._red_move == True:
                            color = "red"
                        else:
                            color = "black"

                        # now we need to check and see if the move moved the
                        # player into check so we will update the board (above)
                        # and then check to see if that color is in check
                        # so if black moved, we check to see whether black is in
                        # check as if it is red's next move.
                        # If black moved into check, we will reverse the move

                        in_check = self.is_in_check(color)
                        if in_check == True:
                            # print("can't move into check")
                            self.set_board_reverse(x, y, x_end, y_end, prev_start, prev_end)
                            # print("board should be reversed")
                            return False
                        else:
                            # updates the color
                            self.set_red_move()
                            return True

    def is_in_check(self, color):
        """
        :param color: This will be a string representation of a color which will
        be used to determine if that color's king is in check
        :return:
        If the king of the chosen color is in check, it will return True
        Otherwise, it will return False
        Action: Once this function determines where the king is, it will then
        loop through each piece of the opposite color to determine if that piece
        has a valid move to the king (i.e. ending coordinates). If it does, the
        king is in check. It will call the special_is_in_check helper function
        to actually validate each move
        """

        #Initialize both the king and the attacking piece to y=0, and x=0.
        #This will place each piece in the top left corner
        #Remember Y is the first coordinate because it does row first in the
        #nested lists and then column (since it is the element in nested list
        king_piece = self._board[0][0]
        attack_piece = self._board[0][0]
        king_color = color
        attack_color = ""

        #sets the attack piece color opposite of color
        if king_color == "red":
            attack_color = "black"
        elif king_color == "black":
            attack_color = "red"

        #First we need to locate the king of the appropriate color
        for coord_y in range(0, 10): #traverses the y coordinates
            for coord_x in range(0, 9): #traverses the x coordinates
                int_piece = self._board[coord_y][coord_x]
                if int_piece == "":
                    piece = coord_y
                    #print("string", coord_y, coord_x)
                else:
                    #print(int_piece.get_type())
                    if int_piece.get_color() == king_color and int_piece.get_type() == "king":
                        king_piece = self._board[coord_y][coord_x]
                        king_y = coord_y
                        king_x = coord_x
                        break

        # Next we need to test each piece of the opposite color for a valid
        # move to the king's location. So the king's location is used as the end
        # coordinates, it it is a valid move the king is in check

        for coord_y in range(0, 10):  # traverses the y coordinates
            for coord_x in range(0, 9):  # traverses the x coordinates
                int_piece = self._board[coord_y][coord_x]
                if int_piece == "":
                    piece = coord_y
                else:
                    if int_piece.get_color() == attack_color:
                        special_check = self.special_check_move(coord_x, coord_y, king_x, king_y, int_piece)
                        if special_check == True:
                            #print("King is in check", int_piece.get_name())
                            #print(True)
                            return True
                        else:
                            king = 3
                            pass
        #print(False)
        return False

    def special_check_move(self, coord_x, coord_y, king_x, king_y, int_piece):
        """
        :param coord_x: Opposite color piece starting x
        :param coord_y: Opposite color piece starting y
        :param king_x: location of king x
        :param king_y: location of king y
        :return: This helper function is given the ending coordinates of a king,
        and a piece of the opposite color as starting coordinates. This function
        will determine if that piece has a valid move to the king
        (i.e. ending coordinates). If it does, the king is in check and It will
        return True to the is_in_check function
        """
        x = coord_x
        y = coord_y
        x_end = king_x
        y_end = king_y
        piece = self._board[y][x]
        king = self._board[y_end][x_end]
        #print("SPECIAL", piece.get_type(), king.get_type())

        if piece.get_type() == "rook":
            valid = piece.rook_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("rook false")
                return False
            else:
                # Call this function to ensure there is no intervening piece
                special_rook = self.special_rook_move(x, y, x_end, y_end, piece)
                if special_rook == False:
                    #print("rook false")
                    return False
                else:
                    #print("rook True")
                    return True

        elif piece.get_type() == "pawn":
            valid = piece.pawn_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("pawn false")
                return False
            else:
                #print("pawn true")
                return True

        elif piece.get_type() == "cannon":
            valid = piece.cannon_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("cannon false")
                return False
            else:
                # Call this function to ensure there is no intervening piece
                special_cannon = self.special_cannon_move(x, y, x_end, y_end, piece)
                if special_cannon == False:
                    #print("cannon false")
                    return False
                else:
                    #print("cannon true")
                    return True

        elif piece.get_type() == "king":
            valid = piece.king_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("King False")
                return False
            else:
                #print("KIng True")
                return True

        elif piece.get_type() == "bishop":
            valid = piece.bishop_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("bishop false")
                return False
            else:
                # Call this function to ensure there is no intervening piece
                special_bishop = self.special_bishop_move(x, y, x_end, y_end, piece)
                if special_bishop == False:
                    #print("bishop false")
                    return False
                else:
                    #print("bishop true")
                    return True

        elif piece.get_type() == "guard":
            valid = piece.guard_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("guard false")
                return False
            else:
                #print("guard true")
                return True

        elif piece.get_type() == "knight":
            valid = piece.knight_valid_move(x, y, x_end, y_end, piece)
            if valid == False:
                #print("knight false")
                return False
            else:
                # Call this function to ensure there is no intervening piece
                special_knight = self.special_knight_move(x, y, x_end, y_end, piece)
                if special_knight == False:
                    #print("knight false")
                    return False
                else:
                    #print("knight valid")
                    return True


class Piece:
    """The Piece class is the parent class for all individual pieces. It will
    initiate each piece with a name (such as RK for red king, BP for black pawn,
    etc.),  a color of "red" or "black", a distinct type, such as "rook" or
     "bishop" which will be used to put it into the proper subclass. Finally,
     each piece must be initialized with a distinct location in algebraic
     notation. This will be used tp initialize the piece and place it on the
     board in the game class.
     The piece class will also have get methods for color, type, name, and
     position. This will be inherited by all piece subclasses. """
    def __init__(self, name, color, type, position = None):
        self._name = name
        self._color = color
        self._type = type
        self._position = position

    def __repr__(self):   #print piece on board instead of object reference
        return self._name

    def get_name(self):
        """returns the name of the selected piece (RK, BK, etc.). All names
        will be initialized to being with R for Red or B for Black and then
        one letter for the piece K-King, P-pawn, B-Bishop, C-Cannon, R-Rook,
         G-guard, K-knight"""
        return self._name

    def get_color(self):
        """returns the color of the selected piece ("red" or black")."""
        return self._color

    def get_type(self):
        """returns the type of the selected piece: "king", "pawn", "bishop",
         "cannon", "rook", "guard", and  "knight"   """
        return self._type

    def get_position(self):
        """returns the position of the piece"""
        return self._position


class Rook(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the rook move is legal,
    without any reference to the board. The legality of the move in relation
    to other pieces will be dealt with in the Game Class, which creates and
    manages the board.
    Rook's legal moves:  move and capture any distance orthongonally
    Rooks's Special Move: may not  jump an intervening piece. This will be
        dealt with in the Game Class, NOT HERE"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def rook_valid_move(self, x1, y1, x2, y2, piece):
        """
        Rook's legal moves:  move and capture any distance orthongonally
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        #print(x1, y1, x2, y2)
        if x1 != x2 and y1 != y2:
            #print("cant move")
            return False
        elif x1 == x2 and y1 == y2:
            #print("not ok")
            return False
        return


class Pawn(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the pawn move is legal,
    without any reference to the board. The legality of the move in relation
    to other pieces will be dealt with in the Game Class, which creates and
    manages the board.
    Pawns's legal moves:  They move and capture by advancing one point.
        Once they have crossed the river, they may also move and capture
        one point horizontally. Pawns cannot move backward

    Pawns's Special Move: See change after crossing river. This will be
        dealt with in this subclass"""
    def __init__(self, name, color, type, position=None):
        super().__init__(name, color, type, position)

    def pawn_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  move and capture by advancing one point.
        Once they have crossed the river, they may also move and capture
        one point horizontally. Soldiers cannot move backward
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        if piece.get_color() == "red":
            #print(x1, y1, x2, y2, "red")
            if y1 == 5 or y1 == 6: #precrossing the river
                if y2 != (y1 - 1) or x1 != x2:
                    #print("cant move preriver")
                    return False
                else:
                    throwaway = 2
                    #print("valid Pre-river")
            else: #after the pawn crosses the river
                if y2 == (y1 - 1) and x2 == x1:
                    #print("validpostY")
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    #print("validpostX-1")
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    #print("validpostX+1")
                    return
                else:
                    #print("cant move postriver")
                    return False
        if piece.get_color() == "black":
            #print(x1, y1, x2, y2, "black")
            if y1 == 3 or y1 == 4: #precrossing the river
                if y2 != (y1 + 1) or x1 != x2:
                    #print("cant move preriver")
                    return False
                else:
                    #print("valid Pre-river")
                    throw = 2 #throwaway
            else: #after the pawn crosses the river
                if y2 == (y1 + 1) and x2 == x1:
                    #print("validpostY")
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    #print("validpostX-1")
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    #print("validpostX+1")
                    return
                else:
                    #print("cant move postriver")
                    return False


class Knight(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the knight move is legal,
    without any reference to the board. The legality of the move in relation
    to other pieces will be dealt with in the Game Class, which creates and
    manages the board.
    Knights's legal moves:  moves and captures one point orthogonally and
            then one point diagonally
    Knight's Special Move: may not jump an intervening piece. This will be
        dealt with in the Game Class, NOT HERE"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def knight_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  moves and captures one point orthogonally and
            then one point diagonally
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        if x2 == (x1 - 1) and y2 == (y1 - 2):
            #print("UL")
            return
        elif x2 == (x1 + 1) and y2 == (y1 - 2):
            #print("UR")
            return
        elif x2 == (x1 + 2) and y2 == (y1 - 1):
            #print("RU")
            return
        elif x2 == (x1 + 2) and y2 == (y1 + 1):
            #print("RD")
            return
        ###########################
        elif x2 == (x1 + 1) and y2 == (y1 + 2):
            #print("DR")
            return
        elif x2 == (x1 - 1) and y2 == (y1 + 2):
            #print("DL")
            return
        elif x2 == (x1 - 2) and y2 == (y1 + 1):
            #print("LD")
            return
        elif x2 == (x1 - 2) and y2 == (y1 - 1):
            #print("LU")
            return
        else:
            return False


class Bishop(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the bishop move is legal,
    without any reference to the board. The legality of the move in relation
    to other pieces will be dealt with in the Game Class, which creates and
    manages the board.
    Bishop's legal moves:  move and capture exactly two points diagonally
    Bishop's Special Move: may not  jump an intervening piece. This will be
        dealt with in the Game Class, NOT HERE"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def bishop_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  moves and captures two points diagonally. May not jump an
        intervening piece but that will be dealt with in Game Class
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        if piece.get_color() == "red":
            #print(x1, y1, x2, y2, "red")
            if y2 <= 4:  # can not cross the river
                #print("can't cross river")
                return False
            else:
                #print(x1, y1, x2, y2, "diagonal")
                if x2 == x1 or y2 == y1: #cant go stright in either direction
                    #print("cant go straight")
                    return False
                elif x2 == (x1 - 2) and y2 == (y1 - 2):
                    #print("TL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 - 2):
                    #print("TR")
                    return
                elif x2 == (x1 - 2) and y2 == (y1 + 2):
                    #print("BL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 + 2):
                    #print("BR")
                    return
                else:
                    return False
        elif piece.get_color() == "black":
            #print(x1, y1, x2, y2, "black")
            if y2 >= 5:  # can not cross the river
                #print("can't cross river")
                return False
            else:
                #print(x1, y1, x2, y2, "diagonal")
                if x2 == x1 or y2 == y1: #cant go stright in either direction
                    #print("cant go straight")
                    return False
                elif x2 == (x1 - 2) and y2 == (y1 - 2):
                    #print("TL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 - 2):
                    #print("TR")
                    return
                elif x2 == (x1 - 2) and y2 == (y1 + 2):
                    #print("BL")
                    return
                elif x2 == (x1 + 2) and y2 == (y1 + 2):
                    #print("BR")
                    return
                else:
                    return False


class King(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the king move is legal.
    The legality of the move in relation to other pieces will be dealt with
        in the Game Class, which creates and manages the board.
    king's legal moves:  move and capture one point orthongonally
        and may not leave the palace"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def king_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  moves and captures one point orthongonally. May not leave
        the palace, that is dealt with here
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        if piece.get_color() == "red":
            #print(x1, y1, x2, y2, "red king")
            if x2 <= 2 or x2 >= 6:  # can not leave palace left or right
                #print("can't leave palace x")
                return False
            elif y2 <= 6:  # can not leave palace up
                #print("can't leave palace y")
                return False
            else:
                #print(x1, y1, x2, y2, "valid move")
                if y2 == (y1 - 1) and x2 == x1:
                    return
                elif y2 == (y1 + 1) and x2 == x1:
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    return
                else:
                    return False
        if piece.get_color() == "black":
            #print(x1, y1, x2, y2, "black king")
            if x2 <= 2 or x2 >= 6:  # can not leave palace left or right
                #print("can't leave palace x")
                return False
            elif y2 >= 3:  # can not leave palace down
                #print("can't leave palace y")
                return False
            else:
                #print(x1, y1, x2, y2, "valid move")
                if y2 == (y1 - 1) and x2 == x1:
                    return
                elif y2 == (y1 + 1) and x2 == x1:
                    return
                elif x2 == (x1 - 1) and y2 == y1:
                    return
                elif x2 == (x1 + 1) and y2 == y1:
                    return
                else:
                    return False


class Guard(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the guard move is legal.
    The legality of the move in relation to other pieces will be dealt with
        in the Game Class, which creates and manages the board.
    Guard's legal moves:  move and capture one point diagonally
        and may not leave the palace.
    """
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def guard_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  moves and captures one point diagonally. May not leave
        the palace. That is dealt with here
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        #print(x1, y1, x2, y2)
        if piece.get_color() == "red":
            #print(x1, y1, x2, y2, "red guard")
            if x2 <= 2 or x2 >= 6:  # can not leave palace left or right
                #print("can't leave palace x")
                return False
            elif y2 <= 6:  # can not leave palace up
                #print("can't leave palace y")
                return False
            else:
                #print(x1, y1, x2, y2, "valid move")
                if x2 == (x1 - 1) and y2 == (y1 - 1):
                    #print("TL")
                    return
                elif x2 == (x1 + 1) and y2 == (y1 - 1):
                    #print("TR")
                    return
                elif x2 == (x1 - 1) and y2 == (y1 + 1):
                    #print("BL")
                    return
                elif x2 == (x1 + 1) and y2 == (y1 + 1):
                    #print("BR")
                    return
                else:
                    return False

        if piece.get_color() == "black":
            #print(x1, y1, x2, y2, "black guard")
            if x2 <= 2 or x2 >= 6:  # can not leave palace left or right
                #print("can't leave palace x")
                return False
            elif y2 >= 3:  # can not leave palace down
                #print("can't leave palace y")
                return False
            else:
                #print(x1, y1, x2, y2, "valid move")
                if x2 == (x1 - 1) and y2 == (y1 - 1):
                    #print("TL")
                    return
                elif x2 == (x1 + 1) and y2 == (y1 - 1):
                    #print("TR")
                    return
                elif x2 == (x1 - 1) and y2 == (y1 + 1):
                    #print("BL")
                    return
                elif x2 == (x1 + 1) and y2 == (y1 + 1):
                    #print("BR")
                    return
                else:
                    return False


class Cannon(Piece):
    """This piece subclass inherits all methods and members from Piece. The sole
    purpose of this subclass is to validate that the cannon move is legal,
    without any reference to the board. The legality of the move in relation
    to other pieces will be dealt with in the Game Class, which creates and
    manages the board.
    Cannon's legal moves:  any distance orthogonally without jumping.
    Cannon Special Move: must jump a single piece to capture. This will be
        dealt with in the Game Class, NOT HERE"""
    def __init__(self, name, color, type, position = None):
        super().__init__(name, color, type, position)

    def cannon_valid_move(self, x1, y1, x2, y2, piece):
        """
        Legal moves:  any distance orthogonally without jumping.
        Cannon Special Move: must jump a single piece to capture. This will be
        dealt with in the Game Class, NOT HERE
        :input: starting x,y, ending x2, y2, and piece
        :return: False if any move violates legal move
        """
        #print(x1, y1, x2, y2)
        if x1 != x2 and y1 != y2:
            #print("cant move")
            return False
        elif x1 == x2 and y1 == y2:
            #print("not ok")
            return False
        return True

"""
game = XiangqiGame()
game.print_board() #starting board


################################################################################
#################      TESTING GAME      ##########################
################################################################################

game.make_move('c1', 'e3')
game.print_board()
game.make_move('e7', 'e6')
game.print_board()
game.make_move('b1', 'd2')
game.print_board()
game.make_move('h10', 'g8')
game.print_board()
game.make_move('h1', 'i3')
game.print_board()
game.make_move('g10', 'e8')
game.print_board()
game.make_move('h3', 'g3')
game.print_board()
game.make_move('i7', 'i6')
game.print_board()
game.make_move('i1', 'h1')
game.print_board()
game.make_move('g7', 'g6')
game.print_board()
game.make_move('d2', 'f3')
game.print_board()
game.make_move('h8', 'i8')
game.print_board()


game.make_move('d1', 'e2')
game.print_board()


game.make_move('b8', 'd8')
game.print_board()
game.make_move('a1', 'd1')
game.print_board()
game.make_move('b10', 'c8')
game.print_board()
game.make_move('g4', 'g5')
game.print_board()
game.make_move('d10', 'e9')
game.print_board()
game.make_move('g5', 'g6')
game.print_board()
game.make_move('g8', 'f6')
game.print_board()
game.make_move('g3', 'g2')
game.print_board()
game.make_move('f6', 'e4')
game.print_board()
game.make_move('d1', 'd4')
game.print_board()
game.make_move('a10', 'b10')
game.print_board()

game.make_move('d4', 'e4')
game.print_board()

game.make_move('i8', 'i4')
game.print_board()
game.make_move('e1', 'd1')
game.print_board()
game.make_move('b10', 'b3')
game.print_board()
game.make_move('f3', 'e5')
game.print_board()
game.make_move('i10', 'i7')
game.print_board()
game.make_move('h1', 'h10')
game.print_board()
game.make_move('e6', 'e5')
game.print_board()
game.make_move('h10', 'f10')
game.print_board()
game.make_move('e10', 'f10')
game.print_board()
game.make_move('e4', 'i4')
game.print_board()
game.make_move('a7', 'a6')
game.print_board()

game.make_move('d1', 'e1')
game.print_board()
game.make_move('i7', 'd7')
game.print_board()
game.make_move('c4','c5')
game.print_board()
game.make_move('b3', 'b1')
game.print_board()
game.make_move('e2', 'd1')
game.print_board()
game.make_move('b1', 'd1')
game.print_board()
#king is in check
#try to move something else
game.make_move('i4', 'i6')
game.print_board()

#try to move king but into other check
game.make_move('e1', 'd1')
game.print_board()

#moves the king out of check
game.make_move('e1', 'e2')
game.print_board()
"""

"""
################################################################################
#################      TESTING MOVING INTO CHECK      ##########################
################################################################################

#ROOK
game.make_move("e4", "e5")
game.print_board()


game.make_move("c7", "c6")
game.print_board()

game.make_move("e5", "e6")
game.print_board()

game.make_move("e7", "e6")
game.print_board()

game.make_move("a1", "a2")
game.print_board()

game.make_move("e6", "e5")
game.print_board()

game.make_move("a2", "e2")
game.print_board()

game.make_move("a10", "a9")
game.print_board()

game.make_move("i4", "i5")
game.print_board()

game.make_move("a9", "e9")
game.print_board()

game.make_move("i5", "i6")
game.print_board()

game.make_move("e5", "d5")
game.print_board()

#try to move into check by moving red rook out of way, fails
game.make_move("e2", "f2")
game.print_board()

#gives red a new turn, works
game.make_move("e2", "e3")
game.print_board()
"""
"""
#PAWN
#test pawn by moving blacks pawn back into the way
game.make_move("d5", "e5")
game.print_board()

game.make_move("e3", "e2")
game.print_board()

#move the black rook out of the way
game.make_move("e9", "d9")
game.print_board()

game.make_move("e2", "e4")
game.print_board()

#test pawn by moving blacks pawn and putting black in check
game.make_move("e5", "d5")
game.print_board()

#throwaway black move to make sure it is still blacks turn
game.make_move("a7", "a6")
game.print_board()

game.make_move("e6", "d6")
game.print_board()

#black pawn
game.make_move("e7", "e6")
game.print_board()

game.make_move("e6", "e5")
game.print_board()


#moving the pawn out of the way----should be invalid
game.make_move("e5", "d5")
game.print_board()

#moving the rook in the way to make for a valid pawn move

game.make_move("a1", "a2") #rook
game.print_board()

game.make_move("a2", "e2") #move rook in fron of king
game.print_board()

game.make_move("e5", "d5") #now this pawn move should be valid
game.print_board()

game.is_in_check('black') #returns True
"""


"""
################################################################################
#################      TESTING CHECK      ######################################
################################################################################

game.is_in_check('black')

game.make_move("e4", "e5")
game.print_board()

game.make_move("e5", "e6")
game.print_board()

game.make_move("e6", "d6")
game.print_board()

#black pawn
game.make_move("e7", "e6")
game.print_board()

game.make_move("e6", "e5")
game.print_board()


#moving the pawn out of the way----should be invalid
game.make_move("e5", "d5")
game.print_board()

#moving the rook in the way to make for a valid pawn move

game.make_move("a1", "a2") #rook
game.print_board()

game.make_move("a2", "e2") #move rook in fron of king
game.print_board()

game.make_move("e5", "d5") #now this pawn move should be valid
game.print_board()

game.is_in_check('black') #returns True

#Now I am going to move my black rook into the middle and change color

game.make_move("a10", "a9") #black rook
game.print_board()

game.make_move("a9", "e9") #black rook in front of king
game.print_board()

game.is_in_check('red') #returns False

game.make_move("e2", "a2") #moves the red rook over
game.print_board()

game.is_in_check('red') #returns True
"""


################################################################################
################# ALL BOARD SPECIFIC PIECE TESTING BELOW  ######################
################################################################################

#############     TESTING TWO KINGS NOT FACING EACH OTHER  #####################
"""
#Basically we are moving the two pawns forward and then out of the way
#red pawn
game.make_move("e4", "e5")
game.print_board()

game.make_move("e5", "e6")
game.print_board()

game.make_move("e6", "d6")
game.print_board()

#black pawn
game.make_move("e7", "e6")
game.print_board()

game.make_move("e6", "e5")
game.print_board()


#moving the pawn out of the way----should be invalid
game.make_move("e5", "d5")
game.print_board()

#moving the rook in the way to make for a valid pawn move

game.make_move("a1", "a2") #rook
game.print_board()

game.make_move("a2", "e2") #move rook in fron of king
game.print_board()

game.make_move("e5", "d5") #now this pawn move should be valid
game.print_board()


game.make_move("e2", "e3") #rook move should be valid
game.print_board()


game.make_move("e3", "d3") #rook move should be invalid
game.print_board()
"""



################     CANNON INTERVENING PIECE  #################################
"""
#x is decreasing, cannon moving left across board

game.make_move("h8", "h4") #cannon proper
game.print_board()

game.make_move("h4", "g4") #cannon improper, take but no intervening piece
game.print_board()

game.make_move("h4", "f4") #cannon improper, 1 piece in way and no take
game.print_board()

game.make_move("h4", "c4") #cannon improper, 2 piece in way and take
game.print_board()

game.make_move("h4", "e4") #cannon proper, 1 piece in way and no take
game.print_board()
"""

"""
#x is increasing, cannon moving right across board

game.make_move("b8", "b4") #cannon proper
game.print_board()

game.make_move("b4", "c4") #cannon improper, take but no intervening piece
game.print_board()

game.make_move("b4", "d4") #cannon improper, 1 piece in way and no take
game.print_board()

game.make_move("b4", "g4") #cannon improper, 2 piece in way and take
game.print_board()

game.make_move("b4", "e4") #cannon proper, 1 piece in way and no take
game.print_board()
"""
"""
#y is decreasing, cannon moving up board

game.make_move("b3", "b8") #cannon improper, take but no intervening
game.print_board()

game.make_move("b3", "b9") #cannon improper, piece in way but no take
game.print_board()

game.make_move("b3", "b10") #cannon proper, 1 piece in way and take
game.print_board()
"""
"""
#y is increasing, cannon moving down board

game.make_move("b8", "c8") #cannon proper
game.print_board()

game.make_move("c8", "c5") #cannon improper, piece in way but no take
game.print_board()

game.make_move("c8", "c4") #cannon proper, 1 piece in way and take
game.print_board()
"""

################     ROOK INTERVENING PIECE  #################################
"""
# y decreasing....moving rook up the board
game.make_move("a1", "a3") #rook proper
game.print_board()

game.make_move("a3", "a4") #on pawn invalid
game.print_board()

game.make_move("a3", "a1") #rook proper back to start
game.print_board()

game.make_move("a1", "a6") #past pawn invalid
game.print_board()
"""
"""
#want to move and take with black pawn and then try to go past black pawn
game.make_move("a7", "a6")
game.print_board()

game.make_move("a6", "a5")
game.print_board()

game.make_move("a5", "a4")
game.print_board()

game.make_move("a1", "a6") #past black pawn invalid
game.print_board()

game.make_move("a1", "a4") #take black pawn
game.print_board()
"""
"""
#x is decreasing---moving to left 
game.make_move("i1", "i3") #rook proper
game.print_board()

game.make_move("i3", "g3") #rook improper cannon in way
game.print_board()

game.make_move("h3", "h4") #moves the cannon
game.print_board()


game.make_move("i3", "g3") #rook proper
game.print_board()

#tries to move past the far cannon
game.make_move("g3", "a3") #rook improper
game.print_board()
"""

"""
# x increasing----moving rook right across board
game.make_move("a1", "a3") #rook proper
game.print_board()

#game.make_move("a3", "e3") #rook improper cannon in way
#game.print_board()

game.make_move("b3", "b4") #moves the cannon
game.print_board()

#tries to move past the far cannon
game.make_move("a3", "i3") #rook proper
game.print_board()
"""
"""
# y increasing....moving rook down the board
game.make_move("a10", "a8") #rook proper
game.print_board()

game.make_move("a8", "a7") #on pawn invalid
game.print_board()

game.make_move("a8", "a10") #rook proper back to start
game.print_board()

game.make_move("a10", "a6") #past pawn invalid
game.print_board()
"""




################     KNIGHT INTERVENING PIECE  #################################
"""
#right and then up and down
game.make_move("h1", "i3") #knight proper
game.print_board()

game.make_move("i3", "g2") #move but pawn in way left
game.print_board()
"""

"""
#right and then up and down
game.make_move("b1", "a3") #knight proper
game.print_board()

game.make_move("a3", "c2") #move but pawn in way
game.print_board()


game.make_move("a3", "c5") #move
game.print_board()
"""

"""
#up to left and up to right
game.make_move("b1", "c3") #knight proper
game.print_board()

game.make_move("c3", "b5") #move but pawn in way move left
game.print_board()


game.make_move("c3", "d5") #move king in way
game.print_board()
"""



###############  BISHOP INTERVENING PIECE ######################################

###############   BLACK
#NOTE: RED HAS FULLER TESTING BUT IT IS SAME CODE SO NO NEED.....ALL WORKING
"""
#BLACK TR
game.make_move("g10", "e8") #red right side bishop TL
game.print_board()

game.make_move("e10", "e9") #move king in way
game.print_board()

game.make_move("e9", "f9") #move king in way
game.print_board()

game.make_move("e8", "g10") #red invalid
game.print_board()


#BLACK TL
game.make_move("c10", "e8") #red right side bishop TL
game.print_board()

game.make_move("e10", "e9") #move king in way
game.print_board()

game.make_move("e9", "d9") #move king in way
game.print_board()

game.make_move("e8", "c10") #red invalid
game.print_board()
"""


###############RED###########
"""
#RED BL

game.make_move("c1", "e3") #move bishop
game.print_board()

game.make_move("e1", "e2") #move king in way
game.print_board()

game.make_move("e2", "d2")
game.print_board()

game.make_move("e3", "c1") #bishop back invalid
game.print_board()
"""
"""
#RED BR
game.make_move("g1", "e3") #move bishop
game.print_board()

game.make_move("e1", "e2") #move king in way
game.print_board()

game.make_move("e2", "f2")
game.print_board()

game.make_move("e3", "g1") #bishop back invalid
game.print_board()
"""
"""
#RED TR
game.make_move("e1", "e2") #move king in way
game.print_board()

game.make_move("e2", "d2") #move king in way
game.print_board()

game.make_move("c1", "e3") #red invalid
game.print_board()
"""


"""
#RED TL
game.make_move("g1", "e3") #red right side bishop TL
game.print_board()

game.make_move("e3", "g1") #red right side bishop back BR
game.print_board()

game.make_move("e1", "e2") #move king in way
game.print_board()

game.make_move("e2", "f2") #move king in way
game.print_board()

game.make_move("g1", "e3") #red invalid
game.print_board()
"""

###############  KNIGHT CANNON SWAP SPECIAL MOVE  ##############################
"""
###################Same Side####################################################
game.make_move("b1", "b3") #red valid same side
game.print_board()

game.make_move("h3", "h1") #red valid same side
game.print_board()

game.make_move("b10", "b8") #black valid same side
game.print_board()

game.make_move("h8", "h10") #black valid same side
game.print_board()

###################Across the board############################################
game.make_move("b1", "h3") #red valid across
game.print_board()

game.make_move("h8", "b10") #black valid across
game.print_board()
"""

"""
########WONT LET A COLOR RUN INTO THE SAME COLOR AT END POINT###################
game.make_move("a1", "a3") #red valid
game.print_board()

game.make_move("a3", "a4") #red invalid
game.print_board()

game.make_move("a10", "a7") #black invalid
game.print_board()
"""

################################################################################
#################### ALL SUBCLASS PIECE TESTING BELOW  #########################
################################################################################
"""
#################   BLACK GUARD TESTING  ############################

game.make_move("d10", "e9") #down right
game.print_board()

game.make_move("e9", "e10") #fail straight up
game.print_board()

game.make_move("e9", "f9") #fail right
game.print_board()

game.make_move("e9", "e8") #fail left
game.print_board()

game.make_move("e9", "e8") #fail straight down
game.print_board()

game.make_move("e9", "d8") #down left
game.print_board()

game.make_move("d8", "e9") #up right
game.print_board()

game.make_move("e9", "f8") #up left
game.print_board()


game.make_move("f8", "g7") #fail out of palace
game.print_board()

game.make_move("f8", "d10") #fail two spaces diagonal down right
game.print_board()
"""

"""
#################   RED GUARD TESTING  ############################

game.make_move("d1", "e2") #up right
game.print_board()

game.make_move("e2", "e3") #fail straight up
game.print_board()

game.make_move("e2", "f2") #fail right
game.print_board()

game.make_move("e2", "d2") #fail left
game.print_board()

game.make_move("e2", "e1") #fail straight down
game.print_board()

game.make_move("e2", "f1") #down right
game.print_board()

game.make_move("f1", "e2") #up left
game.print_board()

game.make_move("e2", "d3") #up left
game.print_board()

game.make_move("d3", "c4") #fail out of palace
game.print_board()

game.make_move("d3", "f1") #fail two spaces diagonal down right
game.print_board()
"""



"""
#################   BLACK KING TESTING  ############################
game.make_move("e10", "e9") #down
game.print_board()

game.make_move("e9", "d9") #left
game.print_board()

game.make_move("d9", "c9") #fail---leave palace left
game.print_board()

game.make_move("d9", "e9") #right
game.print_board()

game.make_move("e9", "f9") #right
game.print_board()

game.make_move("f9", "g9") #fail leave palace right
game.print_board()

game.make_move("f9", "f8") #down
game.print_board()

game.make_move("f8", "f7") #fail leave palace down
game.print_board()

game.make_move("f8", "f9") #up
game.print_board()
"""

"""
#################   RED KING TESTING  ############################

game.make_move("e1", "e2") #will work up
game.print_board()

game.make_move("e2", "d2") #left
game.print_board()

game.make_move("d2", "c2") #fail---leave palace left
game.print_board()

game.make_move("d2", "e2") #right
game.print_board()

game.make_move("e2", "f2") #right
game.print_board()

game.make_move("f2", "g2") #fail leave the palace right
game.print_board()

game.make_move("f2", "f1") #down
game.print_board()

game.make_move("f1", "f3") #fail two spaces up
game.print_board()

game.make_move("f1", "d1") #fail two spaces left
game.print_board()

game.make_move("f1", "f2") #up
game.print_board()

game.make_move("f2", "f3") #up
game.print_board()

game.make_move("f3", "f4") #fail leave palace up
game.print_board()
"""


"""
#################   BLACK KNIGHT TESTING  ############################

########a few improper moves##################
game.make_move("b10", "c8") #will work down right
game.print_board()

game.make_move("c8", "d7") #one diagonal fail
game.print_board()

game.make_move("c8", "d8") #one right fail
game.print_board()

game.make_move("c8", "b8") #one left fail
game.print_board()

game.make_move("c8", "c9") #one up fail
game.print_board()

game.make_move("c8", "c7") #one down fail
game.print_board()

game.make_move("c8", "g5") #random
game.print_board()

game.make_move("c8", "a6") #random
game.print_board()

################# PROPER MOVES ALL WORK###########
game.make_move("b10", "c8") #will work down right
game.print_board()

game.make_move("c8", "e9") #will work right up
game.print_board()

game.make_move("e9", "g8") #will work right down
game.print_board()

game.make_move("g8", "e9") #will work left up
game.print_board()
"""


"""
#################   RED KNIGHT TESTING  ############################
########a few improper moves##################
game.make_move("b1", "d2") #will work right up
game.print_board()

game.make_move("d2", "e3") #one diagonal fail
game.print_board()

game.make_move("d2", "e2") #one right fail
game.print_board()

game.make_move("d2", "c2") #one left fail
game.print_board()

game.make_move("d2", "d3") #one up fail
game.print_board()

game.make_move("d2", "d1") #one down fail
game.print_board()

game.make_move("d2", "g5") #random
game.print_board()

game.make_move("d2", "a7") #random
game.print_board()


################# PROPER MOVES ALL WORK###########
game.make_move("b1", "d2") #will work right up
game.print_board()

game.make_move("d2", "f3") #will work right up
game.print_board()

game.make_move("f3", "d4") #will work left up
game.print_board()

game.make_move("d4", "e6") #will work up right
game.print_board()

game.make_move("e6", "c5") #will work  left down
game.print_board()

game.make_move("c5", "e6") #will work  right up
game.print_board()

game.make_move("e6", "g5") #will work  right down
game.print_board()


game.make_move("b1", "c3") #will work up right
game.print_board()

game.make_move("c3", "b5") #will work up left
game.print_board()

game.make_move("b5", "c3") #will work down right
game.print_board()

game.make_move("c3", "b1") #will work down left
game.print_board()

game.make_move("c3", "c6") #will work
game.print_board()

game.make_move("c6", "a8") #will work
game.print_board()

game.make_move("a8", "c10") #will work
game.print_board()
"""


"""
#################   BLACK BISHOP TESTING  ############################
#game.make_move("c10", "e5") #cant cross the river
#game.print_board()

#game.make_move("c10", "c9") #cant go straight
#game.print_board()

#game.make_move("c10", "d10") #cant go sideways
#game.print_board()


game.make_move("c10", "e8") #will work
game.print_board()

game.make_move("e8", "c6") #will work
game.print_board()

game.make_move("c6", "a8") #will work
game.print_board()

game.make_move("a8", "c10") #will work
game.print_board()
"""

"""
#################   RED BISHOP TESTING  ############################

game.make_move("c1", "d2") #cant go diagonal 1 spot
game.print_board()

game.make_move("c1", "f4") #cant go diagonal 3 spot
game.print_board()

game.make_move("c1", "e3") #will work
game.print_board()

game.make_move("e3", "e4") #cant go straight
game.print_board()

game.make_move("e3", "h3") #cant go straight
game.print_board()

game.make_move("e3", "a3") #cant go straight
game.print_board()

game.make_move("e3", "c1") #will work go back to start
game.print_board()

game.make_move("c1", "a3") #valid Top Left
game.print_board()

game.make_move("a3", "c5") #valid Top right
game.print_board()

game.make_move("c5", "e3") #valid bottom right
game.print_board()

game.make_move("e3", "c1") #valid bottom left
game.print_board()
"""

"""
############## BLACK CANNON TESTING ######################
game.make_move("b8", "b7")
game.print_board()
game.make_move("b7", "b2")
game.print_board()
game.make_move("b2", "g2")
game.print_board()
game.make_move("g2", "g8")
game.print_board()
game.make_move("g8", "b8")
game.print_board()
game.make_move("b8", "c7")
game.print_board()
"""

"""
############## RED CANNON TESTING ######################
game.make_move("b3", "b4")
game.print_board()
game.make_move("b4", "b8")
game.print_board()
game.make_move("b8", "g8")
game.print_board()
game.make_move("g8", "b8")
game.print_board()
game.make_move("b8", "b4")
game.print_board()
game.make_move("b4", "b1")
game.print_board()
"""

"""
########BLACK PAWN TESTING##################################
game.make_move("a7", "a6") #passes
game.print_board()
game.make_move("a6", "a5")
game.print_board()
game.make_move("a5", "a4")
game.print_board()

game.make_move("a4", "b4")
game.print_board()

game.make_move("b4", "a4")
game.print_board()

game.make_move("a6", "a7")
game.print_board()
game.make_move("a7", "b7")
game.make_move("b7", "a7")

#game.make_move("a7", "a6") #fails
#game.print_board()
"""

"""
########RED PAWN TESTING###################################
game.make_move("a4", "a5")
game.print_board()
game.make_move("a5", "a6")
game.print_board()
game.make_move("a6", "a7")
game.print_board()
game.make_move("a7", "b7")
game.make_move("b7", "a7")
game.print_board()


##################ROOK#####################################
#NOTE I DELETED MOST OF TESTING
#game.make_move("a1", "a2") #rook




#print(game.get_board()) #prints it as a list
"""



