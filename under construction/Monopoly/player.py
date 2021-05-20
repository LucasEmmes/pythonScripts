class player:
    def __init__(self, name):
        self.name = name
        self.money = 30000
        self.position = 0
        self.in_prison = False
        self.properties = []
        self.cards = []
        self.doubles = 0
        self.streets = []
        self.turn = False

    def roll(self):
        pass

    def pay_bail(self):
        pass

    def end_turn(self):
        pass

    def offer_trade(self):
        pass