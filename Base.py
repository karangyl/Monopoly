MOVES = [2,3,4,5,6,7,8,9,10,11,12]

class Board:
    def __init__(self):
        self.players = []
        raise NotImplementedError


class Square:
        def __init__(self,pos):
            return


class Type():
    def __init__(self):
        return

    def is_action(self):
        raise NotImplementedError

    def is_property(self):
        raise NotImplementedError

    def is_misc(self):
        raise NotImplementedError



class Action(Type):
    def __init__(self,own):
        super(Action,self).__init__()
        self.own = own

    def is_action(self):
        return True

    def is_property(self):
        return False

    def is_misc(self):
        return False


class Property(Type):

    def __init__(self, cost, color, house_cost, rent, mortgage, house_1, house_2, house_3, house_4, hotel, owner, name):
        super(Property,self).__init__()
        self.cost = cost
        self.color = color
        self.house_cost = house_cost
        self.mortgage = mortgage
        self.rent = rent
        self.house_1 = house_1
        self.house_2 = house_2
        self.house_3 = house_3
        self.house_4 = house_4
        self.hotel = hotel
        self.owner = owner
        self.name = name

    def is_action(self):
            return False

    def is_property(self):
            return True

    def is_misc(self):
            return False


class Misc(Type):

    def __init__(self,name):
        super(Misc,self).__init__()
        self.name = name

    def is_action(self):
            return False

    def is_property(self):
            return False

    def is_misc(self):
            return True


class Player:

    def __init__(self,name,pos,money,roll,property):
        self.name = name
        self.pos = pos
        self.money = money
        self.roll = roll
        self.property = property
        return

    def moves(self):
        return MOVES


class HeldByPlayer(Player):
    def __init__(self):
        super(HeldByPlayer,self).__init__()


class TreasureChest(Action):

    def __init__(self):
        super(TreasureChest, self).__init__()
        return

    def check(self):
        if Type.is_action()==1:
            return True
        else:
            return False


class CommunityChest(Action):

    def __init__(self):
        super(CommunityChest, self).__init__()
        return

    def Check(self):
        if Type.is_action() == 1:
            return True
        else:
            return False

class Go(Misc,):

