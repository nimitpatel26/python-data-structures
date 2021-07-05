

class Subset:
    def __init__(self, a, target):
        self.a = a
        self.target = target
        self.cache = {0: True}
        self.is_possible(0, self.target)
        print(self.cache[(0, self.target)])


    def is_possible(self, index, target):
        if target < 0 or index >= len(self.a):
            return False
        if target in self.cache:
            return self.cache[(index, target)]

        possible = False
        # include self.a[index]
        new_target = target - self.a[index]
        if new_target == 0:
            return True
        possible = possible or self.is_possible(index + 1, new_target)


        # not include self.a[index]
        possible = possible or self.is_possible(index + 1, target)

        self.cache[(index, target)] = possible
        return possible




