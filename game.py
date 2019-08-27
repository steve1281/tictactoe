#!/usr/bin/env python

from simple import SimpleAI
from computer import ComputerAI

class Game:
    def __init__(self):
        self.PLAYER_X = 'X'
        self.PLAYER_O = 'O'

        self.board = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]
        self.solutions = [(0,1,2), (3,4,5), (6,7,8),
                          (0,3,6), (1,4,7), (2,5,8),
                          (0,4,8), (2,4,6)]
        self.ai = [SimpleAI(self), ComputerAI(self)]
        self.computerAI = None
    
    def select_level(self):
        print()
        print("TIC TAC TOE")
        print()
        print("Level Selection")
        print()
        i = 0
        levels = []
        options = []
        for x in self.ai:
            levels.append(f"{i} = {self.ai[i].description()}")
            options.append(f"{i}")
            i = i +1
        for x in levels:
            print (x)
        while True:
            x = input("Enter desired difficulty: ")
            if not x in options:
                print("Input error.")
            else:
                self.computerAI = self.ai[int(x)]
                break
        print()

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
            if self.board[ix] != self.PLAYER_O and self.board[ix] != self.PLAYER_X:
                self.board[ix] = player
                return True
        print("error")


    def get_computer_player_input(self, player):
        return self.computerAI.get_computer_player_input(player)



game = Game()
game.select_level()

running = True

# assume human is PLAYER_O
# and goes first
while running:
    game.display()
    while not game.get_human_player_input(game.PLAYER_O): pass # get human
    if game.check_win(game.PLAYER_O):
        game.display()
        print("Human wins.")
        break
    if game.check_stale():
        print("Cats game.")
        break
    # get computer
    game.display()
    game.get_computer_player_input(game.PLAYER_X)
    if game.check_win(game.PLAYER_X):
        game.display()
        print("Computer wins.")
        break
    if game.check_stale(): # aka cats game
        game.display()
        print("Cats game.")
        break
