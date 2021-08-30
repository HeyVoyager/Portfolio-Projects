# Author: Michael Hilmes
# Date: 5/27/2021
# Description: Portfolio Project - Create a class for playing the board game Kuba.

import copy

class KubaGame:
    """Class that handles and executes functionality of Kuba board game."""
    def __init__(self, player1, player2):
        """Initializes data members for the game board, player captures, player turn, winner,
        marble, marble count, player names, player colors, and previous board states."""
        self._game_board = [['W', 'W', 'X', 'X', 'X', 'B', 'B'],
                            ['W', 'W', 'X', 'R', 'X', 'B', 'B'],
                            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
                            ['X', 'R', 'R', 'R', 'R', 'R', 'X'],
                            ['X', 'X', 'R', 'R', 'R', 'X', 'X'],
                            ['B', 'B', 'X', 'R', 'X', 'W', 'W'],
                            ['B', 'B', 'X', 'X', 'X', 'W', 'W']]
        self._p1_captures = 0                   # Private members to store red captures for each player
        self._p2_captures = 0
        self._current_turn = None               # Indicates name of next player's turn
        self._winner = None
        self._marble = None
        self._marble_count = (8, 8, 13)         # White, Black, Red marbles remaining
        self._p1 = player1[0]                   # Private members to store player names
        self._p2 = player2[0]
        self._p1_color = player1[1]             # Private members to store player colors
        self._p2_color = player2[1]
        self._previous_board = []               # Holds board state prior to attempted move
        self._prev_previous_board = []          # Holds board state prior to last player move
        self._save_prev_prev_board = []         # Preserve last game state in case of reset

    def print_game_board(self):
        """Prints the current state of the game board. Receives and returns nothing."""
        print(self._game_board[0])
        print(self._game_board[1])
        print(self._game_board[2])
        print(self._game_board[3])
        print(self._game_board[4])
        print(self._game_board[5])
        print(self._game_board[6])

    def get_game_board(self):
        """Receives nothing and returns the current state of the game board."""
        return self._game_board

    def get_previous_board(self):
        """Receives nothing and returns the state of the game
        board prior to most recent attempted play."""
        return self._previous_board

    def get_prev_previous_board(self):
        """Receives nothing and returns the state of the game
        board prior to the previous player's play."""
        return self._prev_previous_board

    def set_previous_board(self, board):
        """Sets the state of the game board prior to the most recent attempted play.
        Receives game board state and returns nothing."""
        self.set_prev_previous_board(self._previous_board)
        self._previous_board = copy.deepcopy(board)

    def set_prev_previous_board(self, board):
        """Sets the state of the game board to the state prior to the previous player's play.
        Receives previous board state and returns nothing."""
        self._save_prev_prev_board = copy.deepcopy(self._prev_previous_board)
        self._prev_previous_board = copy.deepcopy(board)

    def reset_previous_board(self):
        """Receives nothing and resets the state of the game board to the previous state if
        player attempts to undo previous player's move. Returns nothing."""
        self._game_board = copy.deepcopy(self._previous_board)
        self._previous_board = copy.deepcopy(self._prev_previous_board)
        self._prev_previous_board = copy.deepcopy(self._save_prev_prev_board)

    def get_current_turn(self):
        """Receives nothing and returns the name of the player who's turn it is."""
        return self._current_turn

    def set_current_turn(self, player):
        """Receives player name and sets the name of the player
        who's turn it is next. Returns nothing."""
        if player == self._p1:
            self._current_turn = self._p2
        else:
            self._current_turn = self._p1

    def get_player_name(self, player):
        """Receives player name and returns the name of the current player."""
        if player == self._p1:
            return self._p1
        elif player == self._p2:
            return self._p2

    def get_player_color(self, player):
        """Receives player name and returns the color being played by the current player."""
        if player == self._p1:
            return self._p1_color
        elif player == self._p2:
            return self._p2_color

    def is_valid_color(self, player, color):
        """Checks if appropriate marble is being played. Receives player
        name and marble color. Returns True if so, False if not."""
        if player == self._p1:
            if color == self._p1_color:
                return True
            else:
                return False
        elif player == self._p2:
            if color == self._p2_color:
                return True
            else:
                return False

    def get_winner(self):
        """Receives nothing and returns the name of the winner or None if there is no winner yet."""
        return self._winner

    def set_winner(self, player):
        """Sets the winner to the corresponding player's name.
        Receives player name and returns nothing."""
        self._winner = player

    def get_marble(self, coords):
        """Receives board coordinates and returns the marble color at the given
        coordinates. Returns 'X' if space is empty."""
        marble = self._game_board[coords[0]][coords[1]]
        return marble

    def set_marble(self, color, coords):
        """Sets the new marble color (or empty space) at the corresponding coordinates.
        Receives marble color and coordinate to place the marble in. Returns nothing."""
        self._game_board[coords[0]][coords[1]] = color

    def get_marble_count(self):
        """Receives nothing and returns the current marble count based on
        the state of the game board."""
        return self._marble_count

    def set_marble_count(self):
        """Sets the current marble count based on the state of the game board.
        Receives and returns nothing."""
        white = 0
        black = 0
        red = 0
        row = 0
        game_board = self.get_game_board()

        # Iterate through game board and count number of each color or marble
        while row < 7:
            for column in game_board[row]:
                if column == 'W':
                    white += 1
                elif column == 'B':
                    black += 1
                elif column == 'R':
                    red += 1
            row += 1
        self._marble_count = (white, black, red)

    def get_captured(self, player):
        """Receives player name and returns the number of captured red marbles
        for the corresponding player."""
        if player == self._p1:
            return self._p1_captures
        else:
            return self._p2_captures

    def set_captured(self, player):
        """Increment the number of captured red marbles for the corresponding player.
        Receives player name. Returns nothing."""
        if player == self._p1:
            self._p1_captures += 1
        elif player == self._p2:
            self._p2_captures += 1

    def move_forward(self, player, coords):
        """Make forward move for the player on the marble at the passed coordinates.
        Receives player making the move and coordinates of play.  Returns nothing."""
        marble_list = []
        new_coords = coords
        row = coords[0]

        # Create list of marbles to be moved
        while self.get_marble(new_coords) != 'X' and new_coords[0] >= 0:
            marble_list.append(self.get_marble(new_coords))
            new_coords = (new_coords[0] - 1, new_coords[1])
            if new_coords[0] < 0:
                break
        self.set_marble('X', coords)

        # Place marbles in the list
        for item in marble_list:
            row -= 1
            if row >= 0:
                place_coords = (row, coords[1])
                self.set_marble(item, place_coords)
            # If red marble is captured, increment player's count
            elif row < 0 and marble_list[-1] == 'R':
                self.set_captured(player)
            else:
                return

    def move_backward(self, player, coords):
        """Make backward move for the player on the marble at the passed coordinates.
        Receives player making the move and coordinates of play.  Returns nothing."""
        marble_list = []
        new_coords = coords
        row = coords[0]

        # Create list of marbles to be moved
        while self.get_marble(new_coords) != 'X' and new_coords[0] <= 6:
            marble_list.append(self.get_marble(new_coords))
            new_coords = (new_coords[0] + 1, new_coords[1])
            if new_coords[0] > 6:
                break
        self.set_marble('X', coords)

        # Place marbles in the list
        for item in marble_list:
            row += 1
            if row <= 6:
                place_coords = (row, coords[1])
                self.set_marble(item, place_coords)
            # If red marble is captured, increment player's count
            elif row > 6 and marble_list[-1] == 'R':
                self.set_captured(player)
            else:
                return

    def move_right(self, player, coords):
        """Make right move for the player on the marble at the passed coordinates.
        Receives player making the move and coordinates of play.  Returns nothing."""
        marble_list = []
        new_coords = coords
        column = coords[1]

        # Create list of marbles to be moved
        while self.get_marble(new_coords) != 'X' and new_coords[1] <= 6:
            marble_list.append(self.get_marble(new_coords))
            new_coords = (new_coords[0], new_coords[1] + 1)
            if new_coords[1] > 6:
                break
        self.set_marble('X', coords)

        # Place marbles in the list
        for item in marble_list:
            column += 1
            if column <= 6:
                place_coords = (coords[0], column)
                self.set_marble(item, place_coords)
            # If red marble is captured, increment player's count
            elif column > 6 and marble_list[-1] == 'R':
                self.set_captured(player)
            else:
                return

    def move_left(self, player, coords):
        """Make left move for the player on the marble at the passed coordinates.
        Receives player making the move and coordinates of play.  Returns nothing."""
        marble_list = []
        new_coords = coords
        column = coords[1]

        # Create list of marbles to be moved
        while self.get_marble(new_coords) != 'X' and new_coords[1] >= 0:
            marble_list.append(self.get_marble(new_coords))
            new_coords = (new_coords[0], new_coords[1] - 1)
            if new_coords[1] < 0:
                break
        self.set_marble('X', coords)

        # Place marbles in the list
        for item in marble_list:
            column -= 1
            if column >= 0:
                place_coords = (coords[0], column)
                self.set_marble(item, place_coords)
            # If red marble is captured, increment player's count
            elif column < 0 and marble_list[-1] == 'R':
                self.set_captured(player)
            else:
                return

    def is_legal_f_move(self, player, coords):
        """Checks if a legal forward move is being made. Receives player making the move
        and coordinates of play. Returns True if so, False if not."""
        space_below = (coords[0] + 1, coords[1])

        # Check if the space is valid (edge space, or empty adjacent space)
        if space_below[0] <= 6:
            if self.get_marble(space_below) == 'X':
                row = coords[0] - 1
                while row >= 0:
                    space_above = (row, coords[1])
                    if self.get_marble(space_above) == 'X':
                        return True
                    # Check if player attempts to push off their own marble
                    elif row == 0:
                        edge_coords = (0, coords[1])
                        player_color = self.get_player_color(player)
                        check_edge_marble = self.get_marble(edge_coords)
                        if check_edge_marble == player_color:
                            return False
                        else:
                            return True
                    else:
                        row -= 1
            elif self.get_marble(space_below) != 'X':
                return False
        elif space_below[0] > 6:
            return True

    def is_legal_b_move(self, player, coords):
        """Checks if a legal backward move is being made. Receives player making the move
        and coordinates of play. Returns True if so, False if not."""
        space_above = (coords[0] - 1, coords[1])

        # Check if the space is valid (edge space, or empty adjacent space)
        if space_above[0] >= 0:
            if self.get_marble(space_above) == 'X':
                row = coords[0] + 1
                while row <= 6:
                    space_below = (row, coords[1])
                    if self.get_marble(space_below) == 'X':
                        return True
                    # Check if player attempts to push off their own marble
                    elif row == 6:
                        edge_coords = (6, coords[1])
                        player_color = self.get_player_color(player)
                        check_edge_marble = self.get_marble(edge_coords)
                        if check_edge_marble == player_color:
                            return False
                        else:
                            return True
                    else:
                        row += 1
            elif self.get_marble(space_above) != 'X':
                return False
        elif space_above[0] < 0:
            return True

    def is_legal_r_move(self, player, coords):
        """Checks if a legal right move is being made. Receives player making the move
        and coordinates of play. Returns True if so, False if not."""
        space_left = (coords[0], coords[1] - 1)

        # Check if the space is valid (edge space, or empty adjacent space)
        if space_left[1] >= 0:
            if self.get_marble(space_left) == 'X':
                column = coords[1] + 1
                while column <= 6:
                    space_right = (coords[0], column)
                    if self.get_marble(space_right) == 'X':
                        return True
                    # Check if player attempts to push off their own marble
                    elif column == 6:
                        edge_coords = (coords[0], 6)
                        player_color = self.get_player_color(player)
                        check_edge_marble = self.get_marble(edge_coords)
                        if check_edge_marble == player_color:
                            return False
                        else:
                            return True
                    else:
                        column += 1
            elif self.get_marble(space_left) != 'X':
                return False
        elif space_left[1] < 0:
            return True

    def is_legal_l_move(self, player, coords):
        """Checks if a legal left move is being made. Receives player making the move
        and coordinates of play. Returns True if so, False if not."""
        space_right = (coords[0], coords[1] + 1)

        # Check if the space is valid (edge space, or empty adjacent space)
        if space_right[1] <= 6:
            if self.get_marble(space_right) == 'X':
                column = coords[1] - 1
                while column >= 0:
                    space_left = (coords[0], column)
                    if self.get_marble(space_left) == 'X':
                        return True
                    # Check if player attempts to push off their own marble
                    elif column == 0:
                        edge_coords = (coords[0], 0)
                        player_color = self.get_player_color(player)
                        check_edge_marble = self.get_marble(edge_coords)
                        if check_edge_marble == player_color:
                            return False
                        else:
                            return True
                    else:
                        column -= 1
            elif self.get_marble(space_right) != 'X':
                return False
        elif space_right[1] > 6:
            return True

    def is_winner(self):
        """Checks to see if a player has won. Returns True if so, False if not."""
        # Check for number of player1 red captures
        if self._p1_captures == 7:
            winner = self._p1
            self.set_winner(winner)
            return True
        # Check for number of player2 captures
        elif self._p2_captures == 7:
            winner = self._p2
            self.set_winner(winner)
            return True
        # Check if white marbles have all been eliminated
        elif self._marble_count[0] == 0:
            player_1 = self._p1
            player_2 = self._p2
            if self.get_player_color(player_1) == 'W':
                self.set_winner(player_2)
            elif self.get_player_color(player_1) == 'B':
                self.set_winner(player_1)
            return True
        # Check if black marbles have all been eliminated
        elif self._marble_count[1] == 0:
            player_1 = self._p1
            player_2 = self._p2
            if self.get_player_color(player_1) == 'B':
                self.set_winner(player_2)
            elif self.get_player_color(player_1) == 'W':
                self.set_winner(player_1)
            return True
        else:
            return False

    def make_move(self, player, coords, direction):
        """Makes player moves. Receives player name, coordinates of play, and
        direction of move. Returns True if successful, False if unsuccessful."""
        # Check for valid coordinates
        if coords[0] > 6 or coords[0] < 0 or coords[1] > 6 or coords[1] < 0:
            return False

        # Run while loop if there is not yet a winner
        while self._winner is None:

            # Check if it is the appropriate player's turn
            if player == self.get_current_turn() or self.get_current_turn() is None:
                marble_color = self.get_marble(coords)

                # Check if player is playing the correct color marble
                if self.is_valid_color(player, marble_color):
                    self.set_previous_board(self._game_board)

                    # Make move in the forward direction if move is legal
                    if direction == 'F' and self.is_legal_f_move(player, coords) == True:
                        self.move_forward(player, coords)

                        # Check to make sure player isn't undoing last move
                        if self._prev_previous_board != self._game_board:
                            self.set_current_turn(player)  # change player current turn
                            self.set_marble_count()

                            # Check for winner
                            if self.is_winner() == True:
                                #print(player, "wins!")
                                return True
                            return True
                        else:
                            self.reset_previous_board()
                            return False

                    # Make move in the backward direction
                    if direction == 'B' and self.is_legal_b_move(player, coords) == True:
                        self.move_backward(player, coords)

                        # Check to make sure player isn't undoing last move
                        if self._prev_previous_board != self._game_board:
                            self.set_current_turn(player)  # change player current turn
                            self.set_marble_count()

                            # Check for winner
                            if self.is_winner() == True:
                                #print(player, "wins!")
                                return True
                            return True
                        else:
                            self.reset_previous_board()
                            return False

                    # Make move in the right direction
                    if direction == 'R' and self.is_legal_r_move(player, coords) == True:
                        self.move_right(player, coords)

                        # Check to make sure player isn't undoing last move
                        if self._prev_previous_board != self._game_board:
                            self.set_current_turn(player)  # change player current turn
                            self.set_marble_count()

                            # Check for winner
                            if self.is_winner() == True:
                                #print(player, "wins!")
                                return True
                            return True
                        else:
                            self.reset_previous_board()
                            return False

                    # Make move in the left direction
                    if direction == 'L' and self.is_legal_l_move(player, coords) == True:
                        self.move_left(player, coords)

                        # Check to make sure player isn't undoing last move
                        if self._prev_previous_board != self._game_board:
                            self.set_current_turn(player)  # change player current turn
                            self.set_marble_count()

                            # Check for winner
                            if self.is_winner() == True:
                                #print(player, "wins!")
                                return True
                            return True
                        else:
                            self.reset_previous_board()
                            return False

                    else:
                        return False

                else:
                    return False

            else:
                return False

            #return True

        else:
            return False

