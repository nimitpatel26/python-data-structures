


class Knapsack:
    def __init__(self, profits, weights, capacity):
        self.profits = profits
        self.weights = weights
        self.capacity = capacity
        self.cache = {}

        self.solve(0, self.capacity)
        print(self.cache[(0, capacity)])


    def solve(self, index, capacity):
        if index >= len(self.weights):
            return 0

        if (index, capacity) in self.cache:
            return self.cache[(index, capacity)]

        max_profit = 0
        #include index
        new_capacity = capacity - self.weights[index]
        if new_capacity >= 0:
            max_profit = max(max_profit, self.solve(index + 1, new_capacity)) + self.profits[index]

        #exclude index
        max_profit = max(max_profit, self.solve(index + 1, capacity))

        self.cache[(index, capacity)] = max_profit
        return max_profit
