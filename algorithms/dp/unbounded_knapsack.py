
class Knapsack:
    def __init__(self, profits, weights, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.cache = {}


        print(self.get_max_profit(0, self.capacity))

    def get_max_profit(self, index, capacity):
        if index == len(self.weights) or capacity == 0:
            return 0
        if (index, capacity) in self.cache:
            return self.cache[(index, capacity)]

        max_profit = 0
        # include index

        new_capacity = capacity - self.weights[index]
        multiplier = 1
        while new_capacity >= 0:
            max_profit = max(max_profit, self.get_max_profit(index + 1, new_capacity) + self.profits[index] * multiplier)
            new_capacity -= self.weights[index]
            multiplier += 1


        # exclude index
        max_profit = max(max_profit, self.get_max_profit(index + 1, capacity))

        self.cache[(index, capacity)] = max_profit
        return max_profit
