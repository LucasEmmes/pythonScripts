class street:
    def __init__(self, properties, color):
        self.properties = properties
        self.color = color
        self.owner = None

class property_base:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.mortgaged = False
        self.owner = None

    def transfer_to(self, player):
        # change owner
        # check for street ownership
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
    def __init__(self, street, name, price, c0, c1, c2, c3, c4, c5, house_cost):
        super().__init__(name, price)
        self.street = street
        self.rent = [c0, c1, c2, c3, c4, c5]
        self.house_cost = house_cost
        self.num_of_houses = 0

    def get_rent(self, roll):
        if self.mortgaged: return 0
        if self.num_of_houses == 0:
            if self.owner == self.street.owner:
                return self.rent[0]*2
            else:
                return self.rent[0]
        else:
            return self.rent[self.num_of_houses]

    def add_house(self):
        # check if player has sufficient money
        if self.owner.money >= self.house_cost:
        # check if player owns the street
            if self.owner == self.street.owner:
        # check if house rule holds true
                for prop in self.street.properties:
                    if prop.num_of_houses < self.num_of_houses:
                        return False
        # remove money
                self.owner.money -= self.house_cost
        # increase house counter
                self.num_of_houses += 1
                return True
        return False

    def sell_house(self):
        # check if there are any houses to sell
        if self.num_of_houses > 0:
        # check if house rule holds
            for prop in self.street.properties:
                if prop.num_of_houses > self.num_of_houses:
                    return False
        # decrement counter
            self.num_of_houses -= 1
        # add money to owners account
            self.owner.money += int(self.house_cost/2)
            return True
        return False

# Finished
class station(property_base):
    def __init__(self, name, price, rent):
        super().__init__(name, price)
        self.rent = rent

    def get_rent(self, roll):
        if self.mortgaged: return 0
        amount_of_stations = 0
        for prop in self.owner.properties:
            if type(prop) == station:
                amount_of_stations += 1
        if amount_of_stations > 0:
            return self.rent * 2**(amount_of_stations-1)
        else:
            print("YOU DONT OWN ANY STATIONS BRUV")

# Finished
class utility(property_base):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_rent(self, roll):
        if self.mortgaged: return 0
        amount_of_utilities = 0
        for prop in self.owner.properties:
            if type(prop) == utility:
                amount_of_utilities += 1
        if amount_of_utilities == 1:
            return roll*4
        elif amount_of_utilities == 2:
            return roll*10
        else:
            print("YOU DONT OWN ANY UTILITIES BRUV")