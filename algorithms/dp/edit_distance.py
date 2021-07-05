

class EditDistance:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.cache = {}
        print(self.get_edit_distance(0, 0))


    def get_edit_distance(self, i1, i2):
        if i1 == len(self.s1):
            return len(self.s2) - i2
        if i2 == len(self.s2):
            return len(self.s1) - i1

        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]

        if self.s1[i1] == self.s2[i2]:
            self.cache[(i1, i2)] = self.get_edit_distance(i1 + 1, i2 + 1)
            return self.cache[(i1, i2)]

        c1 = self.get_edit_distance(i1 + 1, i2) + 1
        c2 = self.get_edit_distance(i1, i2 + 1) + 1
        c3 = self.get_edit_distance(i1 + 1, i2 + 1) + 1

        self.cache[(i1, i2)] = min(c1, c2, c3)
        return self.cache[(i1, i2)]
