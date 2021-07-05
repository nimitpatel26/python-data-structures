


class Rabin:
    def __init__(self, s):
        self.s = s

    def verify(self, s, pattern):
        return s == pattern

    def is_match(self, pattern):
        pattern_hash = 0
        text_hash = 0
        for i, p in enumerate(pattern):
            pattern_hash += ord(p) * 10 ** (len(pattern) - i - 1)
            text_hash += ord(self.s[i]) * 10 ** (len(pattern) - i - 1)

        if pattern_hash == text_hash and self.verify(self.s[:len(pattern)], pattern):
            return True


        start = 0
        for i in range(len(pattern), len(self.s)):
            text_hash -= ord(self.s[start]) * 10 ** (len(pattern) - 1)
            text_hash *= 10
            text_hash += ord(self.s[i])
            start += 1
            if pattern_hash == text_hash and self.verify(self.s[start:start + len(pattern)], pattern):
                return True
        return False

