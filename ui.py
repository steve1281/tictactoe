

class IOManager:
    def __init__(self, game):
        self.ai = game.ai
        self.board = game.board
        self.PLAYER_X = game.PLAYER_X
        self.PLAYER_O = game.PLAYER_O


    
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
                print()
                return int(x)

    def display(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")


    def get_human_player_input(self, player):
        x = input("Enter position you want: ")
        if x in ['0','1','2','3','4','5','6','7','8', 'q']:
            if x == 'q':
                exit(0)
            ix = int(x)
            if self.board[ix] != self.PLAYER_O and self.board[ix] != self.PLAYER_X:
                self.board[ix] = player
                return True
        print("error")

    def human_win(self):
        self.display()
        print("Human wins!")

    def computer_win(self):
        self.display()
        print("Computer wins!")

    def cats_game(self):
        self.display()
        print("Cats game - no winner.")

