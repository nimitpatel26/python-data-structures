
class CircularQueue:
    def __init__(self, capacity):
        self.front = -1
        self.back = -1
        self.queue = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def enqueue(self, item):
        if self.length == self.capacity:
            return

        if self.length == 0:
            self.front += 1

        self.back = (self.back + 1) % self.capacity
        self.queue[self.back] = item
        self.length += 1

        return True

    def dequeue(self):
        if self.length == 0:
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.length -= 1

        return item

    def is_empty(self):
        return self.length == 0

    def peek(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        return item
