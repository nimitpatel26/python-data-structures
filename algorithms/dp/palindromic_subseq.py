

class Palin:
    def __init__(self, s):
        self.s = s
        self.cache = {}
        print(self.get_longest_subseq(0, len(self.s) - 1))

    def get_longest_subseq(self, start, end):
        if start > end:
            return 0

        if start == end:
            return 1

        if (start, end) in self.cache:
            return self.cache[(start, end)]

        longest_subseq = 0
        if self.s[start] == self.s[end]:
            longest_subseq = 2 + self.get_longest_subseq(start + 1, end - 1)
        else:
            longest_subseq = max(longest_subseq, self.get_longest_subseq(start + 1, end))
            longest_subseq = max(longest_subseq, self.get_longest_subseq(start, end - 1))

        self.cache[(start, end)] = longest_subseq

        return longest_subseq
