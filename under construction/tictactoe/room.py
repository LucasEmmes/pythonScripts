import random
import tictac
import socket

class room:
    def __init__(self):
        self.room_code = hex(random.randrange(0xFFFF))[2:]
        self.p1 = None
        self.p1_conn = None
        self.p2 = None
        self.p2_conn = None
        self.game = None
    
    def connect_player(self, player, conn):
        if not self.p1:
            self.p1 = player
            self.p1_conn = conn
            return True
        elif not self.p2:
            self.p2 = player
            self.p2_conn = conn
            return True
        else:
            return False

    def start_game(self):
        self.game = tictac.tictactoe(self.p1, self.p2)

    def announce(self, announcement):
        try:
            self.p1_conn.send(announcement.encode("utf-8"))
            self.p2_conn.send(announcement.encode("utf-8"))
        except:
            pass
