
import math
class Longest:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        print(self.get_longest(0, -math.inf))

    def get_longest(self, index, highest):
        if index == len(self.a):
            return 0

        if (index, highest) in self.cache:
            return self.cache[(index, highest)]

        longest = -math.inf
        # include a[index]
        if self.a[index] > highest:
            longest = self.get_longest(index + 1, self.a[index]) + 1

        # exclude a[index]
        longest = max(longest, self.get_longest(index + 1, highest))

        self.cache[(index, highest)] = longest
        return longest