
import math

class MinCoins:
    def __init__(self, coins, target):
        self.coins = coins
        self.target = target
        self.cache = {}

        print(self.min_ways(0, self.target))


    def min_ways(self, index, target):
        if target == 0:
            return 0
        if index == len(self.coins):
            return math.inf

        if (index, target) in self.cache:
            return self.cache[(index, target)]

        min_coins = math.inf
        # include coin
        new_target = target - self.coins[index]
        coins_used = 1
        while new_target >= 0:
            min_coins = min(min_coins, self.min_ways(index + 1, new_target) + coins_used)
            new_target = new_target - self.coins[index]
            coins_used += 1

        # exclude coin
        min_coins = min(min_coins, self.min_ways(index + 1, target))

        self.cache[(index, target)] = min_coins
        return min_coins


