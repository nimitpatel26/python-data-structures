

class NumFactors:
    def __init__(self, n):
        self.n = n
        self.cache = {0: 1, 1: 1, 2: 1, 3: 2}
        print(self.solve(self.n))


    def solve(self, n):
        if n in self.cache:
            return self.cache[n]

        one = self.solve(n - 1)
        three = self.solve(n - 3)
        four = self.solve(n - 4)

        self.cache[n] = one + three + four
        return self.cache[n]