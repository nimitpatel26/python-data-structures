
import math
class Bitonic:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        print(self.get_bitonic(0, True, -math.inf))

    def get_bitonic(self, index, going_up, target):
        if index == len(self.a):
            return 0

        if (index, going_up, target) in self.cache:
            return self.cache[(index, going_up, target)]

        longest = 0
        # go up
        if going_up:
            if self.a[index] > target:
                longest = max(longest, self.get_bitonic(index + 1, going_up, self.a[index]) + 1)
            longest = max(longest, self.get_bitonic(index + 1, False, self.a[index]) + 1)

        # go down
        if not going_up:
            if self.a[index] < target:
                longest = max(longest, self.get_bitonic(index + 1, False, self.a[index]) + 1)

        longest = max(longest, self.get_bitonic(index + 1, True, -math.inf))

        self.cache[(index, going_up, target)] = longest
        return longest