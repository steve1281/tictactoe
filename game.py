
PLAYER_X = 'X'
PLAYER_O = 'O'

class Game:
    def __init__(self):
        self.board = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]
        self.solutions = [(0,1,2), (3,4,5), (6,7,8),
                          (0,3,6), (1,4,7), (2,5,8),
                          (0,4,8), (2,4,6)]
        # self.computerAI = ComputerAI(self)
        self.computerAI = SimpleAI(self)
    
    def display(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def check_possible(self, win, player):
        if self.board[win[0]] == player and self.board[win[1]] == player and self.board[win[2]] == win[2]:
            return win[2]
        if self.board[win[1]] == player and self.board[win[2]] == player and self.board[win[0]] == win[0]:
            return win[0]
        if self.board[win[0]] == player and self.board[win[2]] == player and self.board[win[1]] == win[1]:
            return win[1]
        return -1

    def is_win(self, win, player):
        if self.board[win[0]] == player and self.board[win[1]] == player and self.board[win[2]]==player:
            return True

    def check_for_wins(self, player):
        for x in self.solutions:
            print(f"checking {x} result {self.check_possible(x, player)}")
        print()

    def check_win(self, player):
        for x in self.solutions:
            win = self.is_win(x, player)
            if win:
                return True

    def check_stale(self):
        # just check if there are any moves left
        if any(elem in [0,1,2,3,4,5,6,7,8] for elem in self.board):
            return False
        return True

    def get_human_player_input(self, player):
        x = input("Enter position you want: ")
        if x in ['0','1','2','3','4','5','6','7','8']:
            ix = int(x)
            if self.board[ix] != PLAYER_O and self.board[ix] != PLAYER_X:
                self.board[ix] = player
                return True
        print("error")


    def get_computer_player_input(self, player):
        return self.computerAI.get_computer_player_input(player)


from random import randint

class SimpleAI:
    def __init__(self, game):
        self.board = game.board
        self.check_possible = game.check_possible
        self.solutions = game.solutions

    def computer_next_available(self, player):
        possible = []
        for x in range(9):
            if  self.board[x] == x:
                possible.append(x)
        if len(possible):
            r = randint(0, len(possible)-1)
            self.board[possible[r]] = player
            return True
        else:
            return False

    def get_computer_player_input(self, player):
        if self.computer_next_available(player) : return True
        return True

    
class ComputerAI(SimpleAI):

    def computer_winning_move(self, player):
        for x in self.solutions:
            y = self.check_possible(x, player)
            if y > 0:
                self.board[y] = player
                return True
        return False

    def computer_blocking_move(self, player):
        # check for winning moves on the opposing player
        if player == PLAYER_O:
            check_player = PLAYER_X
        else:
            check_player = PLAYER_O

        # if found, block it and return true.
        for x in self.solutions:
            y = self.check_possible(x, check_player)
            if y > 0:
                self.board[y] = player
                return True
        # if not found, return False
        return False

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
        # at this point, there are no moves, this is a Cats game
        return True  # which is fine, just return True.


game = Game()
running = True

# assume human is PLAYER_O
# and goes first
while running:
    game.display()
    while not game.get_human_player_input(PLAYER_O): pass # get human
    if game.check_win(PLAYER_O):
        game.display()
        print("Human wins.")
        break
    if game.check_stale():
        print("Cats game.")
        break
    # get computer
    game.display()
    game.get_computer_player_input(PLAYER_X)
    if game.check_win(PLAYER_X):
        game.display()
        print("Computer wins.")
        break
    if game.check_stale(): # aka cats game
        game.display()
        print("Cats game.")
        break
