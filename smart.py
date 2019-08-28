from random import randint
from simple import SimpleAI
from computer import ComputerAI
    
class SmartAI(ComputerAI):

    def description(self):
        return "Extreme complexity - unbeatable"

    def computer_force_move(self, player):
        possible = []  # collect a list of possible solutions where we could win
        cross_solutions = [( 1, 4, 7), (3, 4, 5)]
        for x in cross_solutions:
            # if the solution has a player and two empty spots its an option
            if self.board[x[0]] == player and self.board[x[1]] == x[1] and self.board[x[2]] == x[2]:
                possible.append(x)
            if self.board[x[0] == x[0]] and self.board[x[1]] == player and self.board[x[2]] == x[2]:
                possible.append(x)
            if self.board[x[0]] == x[0] and self.board[x[1]] == x[1] and self.board[x[2]] == player:
                possible.append(x)
        if len(possible):
            r = randint(0, len(possible) -1)
            for i in range(3):
                if not possible[r][i] == player:
                    self.board[possible[r][i]] = player
                    return True

    def get_computer_player_input(self, player):
        # check if there is a winning move
        if self.computer_winning_move(player): return True
        # check if there is a blocking move
        if self.computer_blocking_move(player): return True
        # force the human to take a move
        if self.computer_force_move(player): return True
        # check if there is a center
        if self.computer_take_center(player): return True
        # check if there is a corner
        if self.computer_take_corner(player): return True
        # choose next available spot
        if self.computer_next_available(player): return True


