from cards import event_card


class gameboard:
    def __init__(self, properties, event_cards, community_cards):
        self.properties = properties
        self.event_cards = event_cards
        self.community_cards = community_cards
        
        self.free_parking_cash = 0
        self.jail = []