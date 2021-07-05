"""
Uses of Linked List
    (1) Dynamic memory allocation
    (2) Implement stacks and queues
    (3) Undo functionality
    (4) Hash table
    (5) Graphs

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, comparator):
        self.length = 0
        self.comparator = comparator
        self.head = None

    def insert(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.length += 1
            return

        tmp_head = self.head
        while tmp_head.next:
            tmp_head = tmp_head.next

        tmp_head.next = Node(item)

    def remove(self, item):
        if self.is_empty():
            return False

        prev = None
        tmp_head = self.head
        while tmp_head.next:
            if self.comparator(item, tmp_head.val):
                if not prev:
                    self.head = tmp_head.next
                else:
                    prev.next = tmp_head.next
                return True

            prev = tmp_head
            tmp_head = tmp_head.next

        if self.comparator(item, tmp_head.val):
            if not prev:
                self.head = tmp_head.next
            else:
                prev.next = tmp_head.next
            return True

        return False

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0
