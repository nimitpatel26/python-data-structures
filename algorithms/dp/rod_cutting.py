

class RodCutting:
    def __init__(self, lengths, prices, target_length):
        self.lengths = lengths
        self.prices = prices
        self.target_length = target_length

        self.dp = [[0 for i in range(len(self.prices) + 1)] for j in range(len(self.prices) + 1)]

        for i in range(1, len(self.prices) + 1):
            for j in range(1, len(self.prices) + 1):
                # include item + remaining weight max profit
                # previous max profit

                max_profit = 0
                if j >= self.lengths[i - 1]:
                    new_capacity = j - self.lengths[i - 1]
                    max_profit = max(max_profit, self.dp[i][new_capacity] + self.prices[i - 1])
                max_profit = max(max_profit, self.dp[i - 1][j])

                self.dp[i][j] = max_profit

        for row in self.dp:
            print(row)