


class CountingSort:
    def __init__(self, a):
        self.a = a

    def sort(self):
        self.count = [0 for i in range(max(self.a) + 1)]
        for num in self.a:
            self.count[num] += 1

        total = 0
        for i, freq in enumerate(self.count):
            total += freq
            self.count[i] = total


        self.newA = [0 for i in self.a]
        for num in self.a:
            self.newA[self.count[num] - 1] = num
            self.count[num] -= 1
        print(self.newA)

