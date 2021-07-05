
class CountSubset:
    def __init__(self, a, target):
        self.a = a
        self.target = target
        self.cache = {}
        print(self.get_subsets(0, self.target))


    def get_subsets(self, index, target):
        if index == len(self.a):
            return 0
        if (index, target) in self.cache:
            return self.cache[(index, target)]

        subsets = 0
        # including index
        new_target = target - self.a[index]
        if new_target == 0:
            subsets += 1
        subsets += self.get_subsets(index + 1, new_target)

        # excluding index
        subsets += self.get_subsets(index + 1, target)

        self.cache[(index, target)] = subsets
        return subsets
