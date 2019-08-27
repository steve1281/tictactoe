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
        levels.append("")
        levels.append("q - Quit")
        options.append('q')
        levels.append("")
        
        for x in levels:
            print (f"\t{x}")
        while True:
            x = input("Enter desired difficulty: ")
            if not x in options:
                print("Input error.")
            else:
                if x == 'q': exit(0)
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


    def game_loop(self):
        self.select_level()
        running = True

        # assume human is PLAYER_O
        # and goes first
        while running:
            self.display()
            while not self.get_human_player_input(self.PLAYER_O): pass # get human
            if self.check_win(self.PLAYER_O):
                self.display()
                print("Human wins.")
                break
            if self.check_stale():
                print("Cats self.")
                break
            # get computer
            self.display()
            self.get_computer_player_input(self.PLAYER_X)
            if self.check_win(self.PLAYER_X):
                self.display()
                print("Computer wins.")
                break
            if self.check_stale(): # aka cats game
                self.display()
                print("Cats self.")
                break

if __name__ == '__main__':
    Game().game_loop()

