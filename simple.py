from random import randint

class SimpleAI:
    def __init__(self, game):
        self.board = game.board
        self.check_possible = game.check_possible
        self.solutions = game.solutions
        self.PLAYER_X = game.PLAYER_X
        self.PLAYER_O = game.PLAYER_O

    def description(self):
        return "Simple - random"

    def computer_next_available(self, player):
        possible = []
        for x in range(9):
            if  self.board[x] == x:
                possible.append(x)
        if len(possible):
            r = randint(0, len(possible)-1)
            self.board[possible[r]] = player
            return True

    def get_computer_player_input(self, player):
        if self.computer_next_available(player) : return True

    

