class Longest:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.n = max(len(s1), len(s2))
        self.dp = [[[-1 for _ in range(self.n)] for _ in range(self.n)] for _ in range(self.n)]
        print(self.get_longest(0, 0, 0))

    def get_longest(self, i1, i2, count):
        if i1 == len(self.s1) or i2 == len(self.s2):
            return count

        if self.dp[i1][i2][count] != -1:
            return self.dp[i1][i2][count]

        c1 = count
        if self.s1[i1] == self.s2[i2]:
            c1 = self.get_longest(i1 + 1, i2 + 1, count + 1)
        c2 = self.get_longest(i1 + 1, i2, count)
        c3 = self.get_longest(i1, i2 + 1, count)
        self.dp[i1][i2][count] = max(c1, c2, c3)
        return self.dp[i1][i2][count]
