

class Palin:
    def __init__(self, s):
        self.s = s
        self.dp = [[False for _ in range(len(self.s) + 1)] for _ in range(len(self.s) + 1)]

        self.count = 0
        self.get_palin_substring_count()

        print(self.count)

    def get_palin_substring_count(self):
        for i in range(len(self.s), 0, -1):
            for j in range(i, len(self.s) + 1):
                if i > j:
                    continue
                if i == j:
                    self.dp[i][j] = True
                    self.count += 1
                    continue

                self.dp[i][j] = False
                if self.s[i - 1] == self.s[j - 1] and (self.dp[i + 1][j - 1] or self.dp[i - 1][j - 1] or j - i == 1):
                    self.dp[i][j] = True
                    self.count += 1








