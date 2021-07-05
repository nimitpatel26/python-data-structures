
import math
class Palin:
    def __init__(self, s):
        self.s = s
        self.n = len(self.s)
        self.dp = [[False for i in range(self.n)] for j in range(self.n)]
        print(self.s)
        self.get_palin()

        cuts = [0 for _ in range(self.n)]
        for start_index in range(self.n - 1, -1, -1):
            min_cuts = self.n  # maximum cuts
            for end_index in range(self.n - 1, start_index - 1, -1):
                if self.dp[start_index][end_index]:
                    # we can cut here as we got a palindrome
                    # also we don't need any cut if the whole substring is a palindrome
                    min_cuts = 0 if end_index == self.n - 1 else min(min_cuts, 1 + cuts[end_index + 1])

            cuts[start_index] = min_cuts
        print(cuts)




        print("")

    def get_palin(self):

        """
        if match:
            dp[i - 1][j - 1] == true ==> true
            j - i == 1 ==> true
        else:
            dp[i + 1][j], dp[i][j - 1]

        """

        for i in range(self.n, -1, -1):
            for j in range(i, self.n):
                if self.s[i] == self.s[j] and (i + 1 >= self.n or self.dp[i + 1][j - 1] or j - i == 1 or i == j):
                    self.dp[i][j] = True

    def get_max(self):
        x, y = -1, -1
        for i in range(self.n):
            for j in range(i, self.n):
                if self.dp[i][j] and j - i + 1 > y - x:
                    x, y = i, j
        return x, y

    def erase(self, x, y):
        for i in range(self.n):
            for j in range(i, self.n):
                if i == x or j == y:
                    self.dp[i][j] = False


