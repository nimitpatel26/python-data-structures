class WordBreak:
    def __init__(self, s, words):
        self.s = s
        self.words = words
        self.cache = {}
        print(self.is_match(s, words))

    def find_matches(self, s, words):
        matches = []
        for w in words:
            is_match = True
            s_index = 0
            for c in w:
                if s_index == len(s):
                    break

                if c != s[s_index]:
                    is_match = False
                    break
                s_index += 1
            if is_match:
                matches.append(w)
        return matches

    def is_match(self, s, words):
        if len(s) == 0:
            return True

        if (s, tuple(words)) in self.cache:
            return self.cache[(s, tuple(words))]

        matches = self.find_matches(s, words)

        for match in matches:
            rest = s[len(match):]
            if self.is_match(rest, words):
                self.cache[(s, tuple(words))] = True
                return True
        self.cache[(s, tuple(words))] = False
        return False
