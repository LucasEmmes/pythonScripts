class gameboard:
    def __init__(self, players, *args):
        self.players = players
        self.properties = [prop for prop in args]
        self.turn = 0

    def roll(self, player):
        pass