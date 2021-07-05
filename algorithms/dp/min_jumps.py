import math


class MinJumps:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        print(self.get_min_jumps(0))

    def get_min_jumps(self, index):
        if index >= len(self.a) - 1:
            return 0

        if self.a[index] == 0:
            return math.inf

        if index in self.cache:
            return self.cache[index]

        min_jumps = math.inf
        jump_limit = self.a[index]
        for j in range(1, jump_limit + 1):
            min_jumps = min(min_jumps, self.get_min_jumps(index + j) + 1)

        self.cache[index] = min_jumps
        return min_jumps
