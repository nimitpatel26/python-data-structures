
class SuperSeq:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.cache = {}
        self.get_super_seq(0, 0)
        val = len(self.s1) - self.cache[(0, 0)] + len(self.s2)
        print(val)

    def get_super_seq(self, i1, i2):
        if i1 == len(self.s1) or i2 == len(self.s2):
            return 0

        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]

        longest = 0
        if self.s1[i1] == self.s2[i2]:
            longest = self.get_super_seq(i1 + 1, i2 + 1) + 1
        longest = max(longest, self.get_super_seq(i1 + 1, i2), self.get_super_seq(i1, i2 + 1))

        self.cache[(i1, i2)] = longest
        return longest


