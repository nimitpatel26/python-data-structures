"""
Uses of Stack:
    (1) Reverse a word
    (2) Calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form
    (3) Browsers use it for back functionality

"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]