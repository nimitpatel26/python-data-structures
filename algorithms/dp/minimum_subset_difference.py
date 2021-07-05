


class Subset:
    def __init__(self, a):
        self.a = a
        self.cache = {}
        self.sum_possible(0, 0, 0)
        print(self.cache[(0, 0)])


    def sum_possible(self, index, sum1, sum2):
        if index == len(self.a):
            return abs(sum1 - sum2)

        if (index, sum1) in self.cache:
            return self.cache[(index, sum1)]

        diff1 = self.sum_possible(index + 1, sum1 + self.a[index], sum2)
        diff2 = self.sum_possible(index + 1, sum1, sum2 + self.a[index])
        diff = min(diff1, diff2)

        self.cache[(index, sum1)] = diff
        return diff