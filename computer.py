from random import randint
from simple import SimpleAI

    
class ComputerAI(SimpleAI):

    def description(self):
        return "Medium complexity - beatable"

    def computer_winning_move(self, player):
        for x in self.solutions:
            y = self.check_possible(x, player)
            if y > 0:
                self.board[y] = player
                return True

    def computer_blocking_move(self, player):
        # check for winning moves on the opposing player
        if player == self.PLAYER_O:
            check_player = self.PLAYER_X
        else:
            check_player = self.PLAYER_O

        # if found, block it and return true.
        for x in self.solutions:
            y = self.check_possible(x, check_player)
            if y > 0:
                self.board[y] = player
                return True

    def computer_take_center(self, player):
        if self.board[4] == 4:
            self.board[4] = player
            return True

    def computer_take_corner(self, player):
        if self.board[0] == 0:
            self.board[0] = player
            return True
        if self.board[2] == 2:
            self.board[2] = player
            return True
        if self.board[6] == 6:
            self.board[6] = player
            return True
        if self.board[8] == 8:
            self.board[8] = player
            return True


    def get_computer_player_input(self, player):
        # check if there is a winning move
        if self.computer_winning_move(player): return True
        # check if there is a blocking move
        if self.computer_blocking_move(player): return True
        # check if there is a center
        if self.computer_take_center(player): return True
        # check if there is a corner
        if self.computer_take_corner(player): return True
        # choose next available spot
        if self.computer_next_available(player): return True


