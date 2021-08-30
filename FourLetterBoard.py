# Author: Michael Hilmes
# Date: 3/1/2021
# Description: Project 10 - Two player game on a 4x4 grid that is won if a player
# fills a row, column, or 2x2 corner region with letters A-D without duplicating a
# letter previously placed by the other player.


class FourLetterBoard:
    """Two player game that is won if player fills row, column, or 2x2 corner region
    with letters A-D without duplicating a letter previously placed by other player"""
    def __init__(self):
        """Initialize private variables"""

        self._game_board = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        self._current_state = "UNFINISHED"
        self._player_o = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        self._player_x = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

    def get_current_state(self):
        """Returns current state of game"""
        return self._current_state

    def is_draw(self, game_board):
        """Check if game is a draw"""
        # Check if all rows have been filled with player moves
        if "" not in game_board[0]:
            if "" not in game_board[1]:
                if "" not in game_board[2]:
                    if "" not in game_board[3]:
                        return True
        else:
            return False

    def is_open_space(self, game_board, row, column):
        """Check if the space is open"""
        if game_board[row][column] == "":
            return True
        else:
            return False

    def legal_play_row(self, player, letter_choice, row):
        """Check if the play is legal for any given row"""
        # Create lists for each row of player o moves
        o_row_0 = [self._player_o[0][0], self._player_o[0][1], self._player_o[0][2], self._player_o[0][3]]
        o_row_1 = [self._player_o[1][0], self._player_o[1][1], self._player_o[1][2], self._player_o[1][3]]
        o_row_2 = [self._player_o[2][0], self._player_o[2][1], self._player_o[2][2], self._player_o[2][3]]
        o_row_3 = [self._player_o[3][0], self._player_o[3][1], self._player_o[3][2], self._player_o[3][3]]
        # Create lists for each row of player x moves
        x_row_0 = [self._player_x[0][0], self._player_x[0][1], self._player_x[0][2], self._player_x[0][3]]
        x_row_1 = [self._player_x[1][0], self._player_x[1][1], self._player_x[1][2], self._player_x[1][3]]
        x_row_2 = [self._player_x[2][0], self._player_x[2][1], self._player_x[2][2], self._player_x[2][3]]
        x_row_3 = [self._player_x[3][0], self._player_x[3][1], self._player_x[3][2], self._player_x[3][3]]

        # For player o moves, check if letter has been played in same row by player x
        if player == "o":
            if row == 0:
                if letter_choice in x_row_0:
                    return False
                else:
                    return True
            elif row == 1:
                if letter_choice in x_row_1:
                    return False
                else:
                    return True
            elif row == 2:
                if letter_choice in x_row_2:
                    return False
                else:
                    return True
            elif row == 3:
                if letter_choice in x_row_3:
                    return False
                else:
                    return True

        # For player o moves, check if letter has been played in same row by player x
        elif player == "x":
            if row == 0:
                if letter_choice in o_row_0:
                    return False
                else:
                    return True
            elif row == 1:
                if letter_choice in o_row_1:
                    return False
                else:
                    return True
            elif row == 2:
                if letter_choice in o_row_2:
                    return False
                else:
                    return True
            elif row == 3:
                if letter_choice in o_row_3:
                    return False
                else:
                    return True

    def legal_play_column(self, player, letter_choice, column):
        """Check if play is legal for any given column"""
        # Create lists for each column of player o moves
        o_column_0 = [self._player_o[0][0], self._player_o[1][0], self._player_o[2][0], self._player_o[3][0]]
        o_column_1 = [self._player_o[0][1], self._player_o[1][1], self._player_o[2][1], self._player_o[3][1]]
        o_column_2 = [self._player_o[0][2], self._player_o[1][2], self._player_o[2][2], self._player_o[3][2]]
        o_column_3 = [self._player_o[0][3], self._player_o[1][3], self._player_o[2][3], self._player_o[3][3]]
        # Create lists for each column of player x moves
        x_column_0 = [self._player_x[0][0], self._player_x[1][0], self._player_x[2][0], self._player_x[3][0]]
        x_column_1 = [self._player_x[0][1], self._player_x[1][1], self._player_x[2][1], self._player_x[3][1]]
        x_column_2 = [self._player_x[0][2], self._player_x[1][2], self._player_x[2][2], self._player_x[3][2]]
        x_column_3 = [self._player_x[0][3], self._player_x[1][3], self._player_x[2][3], self._player_x[3][3]]

        # For player o moves, check if letter has been played in same column by player x
        if player == "o":
            if column == 0:
                if letter_choice in x_column_0:
                    return False
                else:
                    return True
            elif column == 1:
                if letter_choice in x_column_1:
                    return False
                else:
                    return True
            elif column == 2:
                if letter_choice in x_column_2:
                    return False
                else:
                    return True
            elif column == 3:
                if letter_choice in x_column_3:
                    return False
                else:
                    return True

        # For player x moves, check if letter has been played in same column by player o
        elif player == "x":
            if column == 0:
                if letter_choice in o_column_0:
                    return False
                else:
                    return True
            elif column == 1:
                if letter_choice in o_column_1:
                    return False
                else:
                    return True
            elif column == 2:
                if letter_choice in o_column_2:
                    return False
                else:
                    return True
            elif column == 3:
                if letter_choice in o_column_3:
                    return False
                else:
                    return True

    def legal_play_region(self, player, letter_choice, row, column):
        """Check if play is legal for any given 2x2 corner region"""
        # Create lists for each region for player o moves
        o_region_1 = [self._player_o[0][0], self._player_o[0][1], self._player_o[1][0], self._player_o[1][1]]
        o_region_2 = [self._player_o[0][2], self._player_o[0][3], self._player_o[1][2], self._player_o[1][3]]
        o_region_3 = [self._player_o[2][0], self._player_o[2][1], self._player_o[3][0], self._player_o[3][1]]
        o_region_4 = [self._player_o[2][2], self._player_o[2][3], self._player_o[3][2], self._player_o[3][3]]
        # Create lists for each region for player x moves
        x_region_1 = [self._player_x[0][0], self._player_x[0][1], self._player_x[1][0], self._player_x[1][1]]
        x_region_2 = [self._player_x[0][2], self._player_x[0][3], self._player_x[1][2], self._player_x[1][3]]
        x_region_3 = [self._player_x[2][0], self._player_x[2][1], self._player_x[3][0], self._player_x[3][1]]
        x_region_4 = [self._player_x[2][2], self._player_x[2][3], self._player_x[3][2], self._player_x[3][3]]

        # Create variable to store the region of the current play
        region = ""

        # Determine which row the current move was placed
        if row in range(0, 2):
            if column in range(0, 2):
                region = 1
            else:
                region = 2
        elif row in range(2, 4):
            if column in range(0, 2):
                region = 3
            else:
                region = 4

        # For player o moves, check if letter has been played in same region by player x
        if player == "o":
            if region == 1:
                if letter_choice in x_region_1:
                    return False
                else:
                    return True
            elif region == 2:
                if letter_choice in x_region_2:
                    return False
                else:
                    return True
            elif region == 3:
                if letter_choice in x_region_3:
                    return False
                else:
                    return True
            elif region == 4:
                if letter_choice in x_region_4:
                    return False
                else:
                    return True

        # For player x moves, check if letter has been played in same region by player o
        elif player == "x":
            if region == 1:
                if letter_choice in o_region_1:
                    return False
                else:
                    return True
            elif region == 2:
                if letter_choice in o_region_2:
                    return False
                else:
                    return True
            elif region == 3:
                if letter_choice in o_region_3:
                    return False
                else:
                    return True
            elif region == 4:
                if letter_choice in o_region_4:
                    return False
                else:
                    return True

    def is_row_winner(self, game_board):
        """Check if any given row is a winner"""
        # Create individual row lists
        row_1 = [game_board[0][0], game_board[0][1], game_board[0][2], game_board[0][3]]
        row_2 = [game_board[1][0], game_board[1][1], game_board[1][2], game_board[1][3]]
        row_3 = [game_board[2][0], game_board[2][1], game_board[2][2], game_board[2][3]]
        row_4 = [game_board[3][0], game_board[3][1], game_board[3][2], game_board[3][3]]
        # Sort individual row lists
        row_1.sort()
        row_2.sort()
        row_3.sort()
        row_4.sort()
        # Check for a winner in each row list
        if row_1 == ["A", "B", "C", "D"]:
            return True
        elif row_2 == ["A", "B", "C", "D"]:
            return True
        elif row_3 == ["A", "B", "C", "D"]:
            return True
        elif row_4 == ["A", "B", "C", "D"]:
            return True
        else:
            return False

    def is_column_winner(self, game_board):
        """Check if any given column is a winner"""
        # Create individual column lists
        column_1 = [game_board[0][0], game_board[1][0], game_board[2][0], game_board[3][0]]
        column_2 = [game_board[0][1], game_board[1][1], game_board[2][1], game_board[3][1]]
        column_3 = [game_board[0][2], game_board[1][2], game_board[2][2], game_board[3][2]]
        column_4 = [game_board[0][3], game_board[1][3], game_board[2][3], game_board[3][3]]
        # Sort individual column lists
        column_1.sort()
        column_2.sort()
        column_3.sort()
        column_4.sort()
        # Check for a winner in each column list
        if column_1 == ["A", "B", "C", "D"]:
            return True
        elif column_2 == ["A", "B", "C", "D"]:
            return True
        elif column_3 == ["A", "B", "C", "D"]:
            return True
        elif column_4 == ["A", "B", "C", "D"]:
            return True
        else:
            return False

    def is_region_winner(self, game_board):
        """Check if any given 2x2 region is a winner"""
        # Create individual region lists
        region_1 = [game_board[0][0], game_board[0][1], game_board[1][0], game_board[1][1]]
        region_2 = [game_board[0][2], game_board[0][3], game_board[1][2], game_board[1][3]]
        region_3 = [game_board[2][0], game_board[2][1], game_board[3][0], game_board[3][1]]
        region_4 = [game_board[2][2], game_board[2][3], game_board[3][2], game_board[3][3]]
        # Sort the region lists
        region_1.sort()
        region_2.sort()
        region_3.sort()
        region_4.sort()
        # Check for a winner in each region list
        if region_1 == ["A", "B", "C", "D"]:
            return True
        elif region_2 == ["A", "B", "C", "D"]:
            return True
        elif region_3 == ["A", "B", "C", "D"]:
            return True
        elif region_4 == ["A", "B", "C", "D"]:
            return True
        else:
            return False

    def make_move(self, row, column, letter_choice, player):
        """Make the player moves"""
        while self._current_state == "UNFINISHED":          # While loop making moves while game is unfinished
            if player == "o":                               # Player o makes a move
                if not self.is_open_space(self._game_board, row, column):
                    return False
                if not self.legal_play_row(player, letter_choice, row):          # Check for legal play in rows
                    return False
                elif not self.legal_play_column(player, letter_choice, column):  # Check for legal play in columns
                    return False
                elif not self.legal_play_region(player, letter_choice, row, column):   # Check for legal play in regions
                    return False
                else:                                               # If move is legal, add to the game board
                    self._game_board[row][column] = letter_choice   # Add to game board
                    self._player_o[row][column] = letter_choice     # Keep track of player o moves
                    #print(self._game_board)
                    if self.is_row_winner(self._game_board):        # Check if there is a winning row
                        self._current_state = "O_WON"
                        return True
                    elif self.is_column_winner(self._game_board):   # Check if there is a winning column
                        self._current_state = "O_WON"
                        return True
                    elif self.is_region_winner(self._game_board):   # Check if there is a winning region
                        self._current_state = "O_WON"
                        return True
                    elif self.is_draw(self._game_board):            # Check for a draw
                        self._current_state = "DRAW"
                        return True
                    else:
                        return True

            elif player == "x":                             # Player x makes a move
                if not self.is_open_space(self._game_board, row, column):
                    return False
                if not self.legal_play_row(player, letter_choice, row):          # Check for legal play in rows
                    return False
                elif not self.legal_play_column(player, letter_choice, column):  # Check for legal play in columns
                    return False
                elif not self.legal_play_region(player, letter_choice, row, column):   # Check for legal play in regions
                    return False
                else:                                               # If move is legal, add to the game board
                    self._game_board[row][column] = letter_choice   # Add to game board
                    self._player_x[row][column] = letter_choice     # Keep track of player x moves
                    #print(self._game_board)
                    if self.is_row_winner(self._game_board):        # Check if there is a winning row
                        self._current_state = "X_WON"
                        return True
                    elif self.is_column_winner(self._game_board):   # Check if there is a winning column
                        self._current_state = "X_WON"
                        return True
                    elif self.is_region_winner(self._game_board):   # Check if there is a winning region
                        self._current_state = "X_WON"
                        return True
                    elif self.is_draw(self._game_board):            # Check for a draw
                        self._current_state = "DRAW"
                        return True
                    else:
                        return True

#board = FourLetterBoard()
#board.make_move(2,2,'A','o')
#board.make_move(3,2,'C','o')
#board.make_move(2,3,'B','o')
#board.make_move(3,3,'B','x')
#board.make_move(3,3,'D','x')
#board.make_move(2,3,'A','x')
#board.make_move(3,0,'A','x')
#board.make_move(0,1,'B','o')
#board.make_move(0,2,'B','o')
#board.make_move(1,2,'D','o')
#board.make_move(1,3,'D','o')
#board.make_move(2,1,'B','o')
#board.make_move(3,1,'B','o')
#board.make_move(3,2,'B','o')
#board.make_move(3,3,'B','o')
#board.make_move(1,1,'D','o')
#print(board.get_current_state())
