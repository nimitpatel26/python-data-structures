
class Equal:
    def __init__(self, a):
        self.a = a
        self.cache = {}

        self.total = sum(self.a)
        self.possible = True

        if self.total % 2 == 1:
            self.possible = False
            print("False")
        else:
            self.target = self.total // 2

            self.partition(0, self.target)
            print(self.cache)


    def partition(self, index, target):
        if target == 0:
            return True

        if index >= len(self.a):
            return False

        if (index, target) in self.cache:
            return self.cache[(index, target)]

        possible = False
        # include index
        new_target = target - self.a[index]
        possible = possible or self.partition(index + 1, new_target)

        # skip index
        possible = possible or self.partition(index + 1, target)

        self.cache[(index, target)] = possible
        return possible

