

class CoinChange:
    def __init__(self, coins, target):
        self.coins = coins
        self.target = target
        self.cache = {}
        print(self.ways(0, self.target))


    def ways(self, index, target):
        if target == 0:
            return 1
        if index == len(self.coins):
            return 0

        if (index, target) in self.cache:
            return self.cache[(index, target)]

        ways_change = 0
        # include coin
        new_target = target - self.coins[index]
        while new_target >= 0:
            ways_change += self.ways(index + 1, new_target)
            new_target = new_target - self.coins[index]

        # exclude coin
        ways_change += self.ways(index + 1, target)

        self.cache[(index, target)] = ways_change
        return ways_change

