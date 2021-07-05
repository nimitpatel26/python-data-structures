"""
Uses of Queue:
    (1) CPU scheduling
    (2) Synchronization
    (3) Handling of interrupts

Types of Queue:
    (1) Circular Queue := if the last position is full we insert in the first empty position
    (2) Priority Queue := elements are removed based on their priority
    (3) Double Ended Queue := elements that can be removed and inserted from the front or the back

"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)


    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]
