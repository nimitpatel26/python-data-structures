import math


class RibbonCut:
    def __init__(self, ribbons, target):
        self.ribbons = ribbons
        self.target = target
        self.cache = {}

        print(self.max_ribbon_cuts(0, self.target))

    def max_ribbon_cuts(self, index, target):
        if target == 0:
            return 0
        if index == len(self.ribbons):
            return -math.inf

        if (index, target) in self.cache:
            return self.cache[(index, target)]

        max_cuts = -math.inf
        # make the cut
        if target >= self.ribbons[index]:
            result = self.max_ribbon_cuts(index, target - self.ribbons[index])
            if result != -math.inf:
                max_cuts = result + 1

        # don't make the cut
        max_cuts = max(max_cuts, self.max_ribbon_cuts(index + 1, target))

        self.cache[(index, target)] = max_cuts
        return max_cuts
