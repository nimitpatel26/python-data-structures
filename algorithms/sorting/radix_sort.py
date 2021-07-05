
class RadixSort:
    def __init__(self, a):
        self.a = a

    def sort(self):
        digits = len(str(max(self.a)))

        def get_digit(num, i):
            num = str(num)
            if i >= len(num):
                return 0
            i += 1
            return int(num[-i])

        for i in range(digits):
            highest = max(self.a, key=lambda x: get_digit(x, i))
            count = [0 for i in range(get_digit(highest, i) + 1)]
            for num in self.a:
                digit = get_digit(num, i)
                count[digit] += 1

            total = 0
            for j, num in enumerate(count):
                total += num
                count[j] = total

            self.newA = [0 for i in self.a]
            for num in self.a:
                digit = get_digit(num, i)
                self.newA[count[digit] - 1] = num
                count[digit] -= 1

            self.a = self.newA
            self.a.reverse()
        self.a.reverse()
        print(self.a)
