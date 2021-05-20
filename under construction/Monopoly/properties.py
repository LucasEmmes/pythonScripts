class street:
    def __init__(self, properties, owner):
        self.properties = properties
        self.owner = None

    def owned_by_player(self):
        # if owner of all properties is same, return. else 0 or false or none or whatever
        # add street to player streets
        pass

class property_base:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.mortgaged = False
        self.owner = None

    def transfer_to(self, player):
        pass

    def mortgage(self):
        # check if not mortgaged
        # check mortgage box
        # money to owners account
        pass

    def reactivate(self):
        # check if mortgaged
        # check if player has enough money
        # remove money from player
        # uncheck mortgage
        pass

class regular_property(property_base):
    def __init__(self, street, name, price, c0, c1, c2, c3, c4, c5):
        super().__init__(name, price)
        self.street = street
        self.rent = [c0, c1, c2, c3, c4, c5]
        self.num_of_houses = 0

    def get_rent(self, roll):
        pass

    def add_house(self):
        # check if player has sufficient money
        # check if player owns the street
        # check if house rule holds true
        # remove money
        # increase house counter
        pass

    def sell_house(self):
        # check if there are any houses to sell
        # check if house rule holds
        # decrement counter
        # add money to owners account
        pass

class trainstation(property_base):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_rent(self, roll):
        pass

class special(property_base):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_rent(self, roll):
        pass