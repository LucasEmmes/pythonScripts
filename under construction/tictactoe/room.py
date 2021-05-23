import random
import tictac

class room:
    def __init__(self):
        self.room_code = hex(random.randrange(0xFFFF))[2:]
        self.p1 = None
        self.p2 = None
        self.game = None
    
    def connect_player(self, player):
        if not self.p1:
            self.p1 = player
            return True
        elif not self.p2:
            self.p2 = player
            return True
        else:
            return False

    def start_game(self):
        self.game = tictac.tictactoe(self.p1, self.p2)
