class TargetSum:
    def __init__(self, a, target):
        self.a = a
        self.t = target
        self.cache = {}
        print(self.get_num_sets(0, 0))

    def get_num_sets(self, index, total):
        if index == len(self.a):
            if total == self.t:
                return 1
            return 0
        if (index, total) in self.cache:
            return self.cache[(index, total)]

        subsets = 0
        # add index
        subsets += self.get_num_sets(index + 1, total + self.a[index])

        # subtract index

        subsets += self.get_num_sets(index + 1, total - self.a[index])

        self.cache[(index, total)] = subsets
        return subsets
