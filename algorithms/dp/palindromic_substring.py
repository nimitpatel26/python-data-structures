class Palin:
    def __init__(self, s):
        self.s = s
        self.cache = {}
        print(self.get_longest_substring(0, len(self.s) - 1))

    def get_longest_substring(self, start, end):
        if start > end:
            return 0
        if start == end:
            return 1

        # if (start, end) in self.cache:
        #     return self.cache[(start, end)]

        longest_substring = 0
        if self.s[start] == self.s[end]:
            longest = self.get_longest_substring(start + 1, end - 1)
            remaining = end - start - 1
            if longest == remaining:
                longest_substring = remaining + 2

        longest_substring = max(longest_substring, self.get_longest_substring(start + 1, end), self.get_longest_substring(start, end - 1))

        # self.cache[(start, end)] = longest_substring

        return longest_substring
