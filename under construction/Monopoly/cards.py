class event_card:
    def __init__(self, text, money_gained, money_lost, move_to, cross_start, jail_free, jail):
        self.text = text
        self.money_gained = money_gained
        self.money_lost = money_lost
        self.move_to = move_to
        self.cross_start = cross_start
        self.jail_free = jail_free
        self.jail = jail

class community_card(event_card):
    def __init__(self, text, money_gained, money_lost, move_to, cross_start, jail_free, jail, players_pay_you, can_pull_event_card):
        super().__init__(text, money_gained, money_lost, move_to, cross_start, jail_free, jail)
        self.players_pay_you = players_pay_you
        self.can_pull_event_card = can_pull_event_card