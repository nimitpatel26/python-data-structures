
import math

class MaxSum:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        print(self.a)
        print(self.get_max_sum())

    def get_max_sum(self):

        max_total = 0
        for i, first in enumerate(self.a):
            max_val = 0
            total = 0
            for j in range(i, len(self.a)):
                second = self.a[j]
                if second > max_val:
                    max_val = second
                    total += second
            max_total = max(max_total, total)


        return max_total
