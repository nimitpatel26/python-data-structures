
class PatternMatching:
    def __init__(self, s, pattern):
        self.s = s
        self.pattern = pattern
        self.cache = {}
        print(self.get_pattern(0, 0))


    def get_pattern(self, i, p):
        if p == len(self.pattern):
            return 1
        if i == len(self.s):
            return 0
        if (i, p) in self.cache:
            return self.cache[(i, p)]

        matches = 0
        if self.s[i] == self.pattern[p]:
            matches = self.get_pattern(i + 1, p + 1)
        matches += self.get_pattern(i + 1, p)

        self.cache[(i, p)] = matches
        return matches
