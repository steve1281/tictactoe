#!/usr/bin/env python

from simple import SimpleAI
from computer import ComputerAI
from smart import SmartAI 
from ui import IOManager

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
        self.ai = [SimpleAI(self), ComputerAI(self), SmartAI(self)]
        self.computerAI = None
        self.ui = IOManager(self)
    
    def select_level(self):
        level = self.ui.select_level()
        self.computerAI = self.ai[level]

    def display(self):
        self.ui.display()

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
        if self.ui.get_human_player_input(player): return True

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
                self.ui.human_win()
                break
            if self.check_stale():
                self.ui.cats_game()
                break
            # get computer
            self.display()
            self.get_computer_player_input(self.PLAYER_X)
            if self.check_win(self.PLAYER_X):
                self.ui.computer_win()
                break
            if self.check_stale(): # aka cats game
                self.ui.cats_game()
                break

if __name__ == '__main__':
    Game().game_loop()

