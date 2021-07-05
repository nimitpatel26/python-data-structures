

class Longest:
    def __init__(self, s):
        self.s = s
        self.cache = {}
        print(self.get_longest(0, 0))

    def get_longest(self, i1, i2):
        if i1 == len(self.s) or i2 == len(self.s):
            return 0

        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]

        longest = 0
        if i1 != i2 and self.s[i1] == self.s[i2]:
            longest = self.get_longest(i1 + 1, i2 + 1) + 1
        longest = max(longest, self.get_longest(i1 + 1, i2), self.get_longest(i1, i2 + 1))

        self.cache[(i1, i2)] = longest
        return longest
