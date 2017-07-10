import random

class Dice(object):
    def __init__(self):
        # set random seed
        random.seed(0)
    def roll(self):
        return random.randint(1, 6) + random.randint(1, 6)

class Board(object):
    def __init__(self, game):
        # board: dict, [position, info]
        self.length = 40
        self.board = {}
        infos = [  
                PropInfo(1, "Mediterranean Avenue", 60, 50, {0:2, 1:10, 2:30, 3:90, 4:160, 5:250}),
                ]
        for i in infos:
            self.board[i.get_pos()] = i
        for i in range(40):
            if i not in self.board:
                self.board[i] = NIYInfo()

                #1:PropInfo(1, "Baltic Avenue", 60, 50, {0:4, 1:20, 2:60, 3:180, 4:320, 5:450}),
                #2:RailInfo(2, "Reading Railroad", 200, {1:25, 2:50, 3:100, 4:200}),

    def get_position_info(self, pos):
        return self.board[pos]

class Info(object):
    def __init__(self):
        pass

class PropInfo(Info):
    def __init__(self, position, name, cost, house_cost, rent):
        # position: int, distance to the go
        # cost: int, money to buy property
        # house_cost: int, money to build one house
        # rent: dict, rent need to pay depends number of houses
        self.position = position
        self.name = name
        self.cost = cost
        self.house_cost = house_cost
        self.rent = rent

    def get_cost(self):
        return self.cost

    def get_house_cost(self):
        return self.house_cost

    def get_rent(self, num_house):
        return self.rent[num_house]

    def get_pos(self):
        return self.position

class RailInfo(PropInfo):
    def __init__(self, position, name, cost, rent):
        self.position = position
        self.name = name
        self.cost = cost
        self.rent = rent

    def get_rent(self, amount_of_rail):
        return self.rent[amount_of_rail]

class NIYInfo(Info):
    def __init__(self):
        pass

    def get_cost(self):
        return 0

    def get_house_cost(self):
        return 0

    def get_rent(self, num_house):
        return 0

    def get_pos(self):
        return 0

class Prop(object):
    def __init__(self, info, in_color_group):
        self.info = info
        self.asset = self.info.get_cost()
        self.num_house = 0
        self.in_color_group = in_color_group

    def add_house(self):
        self.num_house += 1
        self.asset += self.get_house_cost()

    def sub_house(self):
        self.num_house -= 1
        self.asset -= self.get_house_cost()

    def get_house_cost(self):
        return self.info.get_house_cost()

    def get_asset(self):
        return self.asset

    def get_house_number(self):
        return self.num_house

    def get_rent(self):
        if self.in_color_group and self.num_house == 0:
            return self.info.get_rent(self.num_house) * 2
        return self.info.get_rent(self.num_house)

    def set_color_group(self, in_cg):
        self.in_color_group = in_cg

class RailProp(object):
    def __init__(self, info):
        self.info = info

    def get_asset(self):
        return self.info.cost

    def get_rent(self, num_of_rails):
        return self.info.get_rent(num_of_rails)

class Player(object):
    def __init__(self, name, pos, cash, strategy, board, game):
        self.name = name
        self.pos = pos
        self.cash = cash
        self.properties = []
        self.strategy = strategy
        self.board = board
        self.game = game

    def add_property(self, prop):
        if self.cash >= prop.info.cost:
            self.properties.append(prop)
            self.cash -= prop.info.cost

    def move(self):
        steps = self.game.roll_dice()
        if ((steps + self.pos) >= self.board.length):
            self.pos -= self.board.length
            self.cash += 200
        self.pos += steps
        assert (self.pos >= 0)
        self.strategy.decide(Prop(self.board.get_position_info(self.pos), False), self.cash)

class Strategy(object):
    def __init__(self):
        pass

    def decide(self, prop, cash):
        pass

class Game(object):
    def __init__(self):
        self.strategy = Strategy()
        self.board = Board(self)
        self.players = [Player("Bob", 0, 1500, self.strategy, self.board, self)]
        self.dice = Dice()

    def play(self):
        #while not self.check_win():
        for i in range(1000):
            for player in self.players:
                player.move()

    def check_win(self):
        pass

    def roll_dice(self):
        return self.dice.roll()
