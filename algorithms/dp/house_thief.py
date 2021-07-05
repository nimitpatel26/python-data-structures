
class Thief:
    def __init__(self, wealth):
        self.wealth = wealth
        self.cache = {}
        print(self.optimal_houses(0))


    def optimal_houses(self, index):
        if index >= len(self.wealth):
            return 0

        if index in self.cache:
            return self.cache[index]


        # include index
        w = self.wealth[index] + self.optimal_houses(index + 2)

        # exclude index
        w = max(w, self.optimal_houses(index + 1))

        self.cache[index] = w




        return w