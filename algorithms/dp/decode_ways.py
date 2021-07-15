
class DecodeWays:
    def __init__(self, s):
        self.s = s
        self.cache = {}
        print(self.get_ways(self.s))

    def get_ways(self, s):
        if len(s) <= 1:
            return 1

        if s in self.cache:
            return self.cache[s]

        ways = 0
        first = s[0]
        second = s[1]

        if second == "0" or first == "1" or int(second) <= 6:
            ways += self.get_ways(s[2:])
        if second != "0":
            ways += self.get_ways(s[1:])

        self.cache[s] = ways
        return ways



