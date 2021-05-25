import random

class tictactoe:
    def __init__(self, player1, player2):
        # P1 AND P2 ARE RANDOM INTS USED AS IDENTIFIERS
        self.p1 = player1
        self.p2 = player2

        self.winner = False
        self.done = False
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        if random.randint(0,1):
            self.player_turn = self.p1
            print("PLAYER 1 STARTS")
        else:
            self.player_turn = self.p2
            print("PLAYER 2 STARTS")

    def is_registered_player(self, player):
        if player == self.p1 or player == self.p2:
            return True
        else:
            return False

    def move_turn(self):
        if self.player_turn == self.p1:
            self.player_turn = self.p2
        else:
            self.player_turn = self.p1

    def turn(self, player, position):
        if not self.done:
            x, y = int(position.split(",")[0]), int(position.split(",")[1])
            if self.board[y][x] == 0 and self.player_turn == player:
                self.board[y][x] = player
                self.move_turn()
                print(self.board)
                self.check_win()
                return True
            else:
                return False
        else:
            print("THE GAME IS OVER")
            return False

    def check_win(self):
        win = False
        tie = True

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                print("WON BY VERTICAL")
                win = self.board[0][i]

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                print("WON BY HORISONTAL")
                win = self.board[i][0]

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[2][0] == self.board[1][1] == self.board[0][2]) and self.board[1][1] != 0:
            print("WON BY DIAGONAL")
            win = self.board[1][1]

        if win:
            tie = False
            if win == self.p1:
                self.winner = self.p1
                print("PLAYER 1 WINS!")
            else:
                self.winner = self.p2
                print("PLAYER 2 WINS!")
            self.done = True
        else:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        tie = False
        
        if tie:
            print("TIED")
            self.done = True
