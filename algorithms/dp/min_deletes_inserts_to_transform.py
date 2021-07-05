

class MinTransform:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.n = max(len(s1), len(s2))
        self.dp = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        val = self.get_min_transform(0, 0)
        print(len(self.s1) - val + len(self.s2) - val)


    def get_min_transform(self, i1, i2):
        if i1 == len(self.s1) or i2 == len(self.s2):
            return 0

        if self.dp[i1][i2] != -1:
            return self.dp[i1][i2]

        c1 = 0
        if self.s1[i1] == self.s2[i2]:
            c1 = self.get_min_transform(i1 + 1, i2 + 1) + 1

        c2 = self.get_min_transform(i1 + 1, i2)
        c3 = self.get_min_transform(i1, i2 + 1)
        self.dp[i1][i2] = max(c1, c2, c3)

        return self.dp[i1][i2]



