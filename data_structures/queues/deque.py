"""
Uses of Deque
    (1) Undo redo operations
    (2) Storing history in browsers
    (3) Implement both stacks and queues

"""


class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.front = -1
        self.back = -1
        self.queue = [None] * self.capacity

        pass

    def push_front(self, item):
        if self.is_full():
            return False

        if self.is_empty():
            self.front = 0
            self.back = self.capacity - 1

        self.queue[self.front] = item
        self.front = (self.front + 1) % self.capacity
        self.length += 1

    def push_back(self, item):

        if self.is_full():
            return False

        if self.is_empty():
            self.front = 1
            self.back = 0

        self.queue[self.back] = item
        self.back = (self.back - 1) % self.capacity
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return None
        self.front = (self.front - 1) % self.capacity
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.length -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            return None
        self.back = (self.back + 1) % self.capacity
        item = self.queue[self.back]
        self.queue[self.back] = None
        self.length -= 1
        return item

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

    def peek_front(self):
        if self.is_empty():
            return None
        return self.queue[(self.front - 1) % self.capacity]

    def peek_back(self):
        if self.is_empty():
            return None
        return self.queue[(self.back + 1) % self.capacity]
