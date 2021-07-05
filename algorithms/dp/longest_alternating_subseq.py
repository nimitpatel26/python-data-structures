
import math
class Longest:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        c1 = self.get_longest_alternating(0, True, -math.inf)
        c2 = self.get_longest_alternating(0, False, math.inf)
        print(max(c1, c2))

    def get_longest_alternating(self, index, going_up, target):
        if index == len(self.a):
            return 0
        if (index, going_up, target) in self.cache:
            return self.cache[(index, going_up, target)]

        c1, c2, c3 = 0, 0, 0
        if going_up and self.a[index] > target:
            c1 = self.get_longest_alternating(index + 1, not going_up, self.a[index]) + 1
        if not going_up and self.a[index] < target:
            c2 = self.get_longest_alternating(index + 1, not going_up, self.a[index]) + 1

        c3 = self.get_longest_alternating(index + 1, going_up, -math.inf)

        self.cache[(index, going_up, target)] = max(c1, c2, c3)
        return self.cache[(index, going_up, target)]