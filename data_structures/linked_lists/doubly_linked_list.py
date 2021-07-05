"""
Uses of Doubly Linked List:
    (1) Undo redo operations
    (2) Forward and backwards functionality

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.head.next = self.head
            self.head.prev = self.head
            self.length += 1
            return

        node = Node(item)
        node.next = self.head
        node.prev = self.head.prev

        if self.head.prev:
            self.head.prev.next = node
        self.head.prev = node
        self.length += 1

        return

    def remove(self, item):
        if self.is_empty():
            return False

        if self.length == 1:
            if self.head.val == item:
                self.head = None
                self.length -= 1
                return True
            return False

        tmp_head = self.head
        for i in range(self.length):
            if tmp_head.val == item:
                tmp_head.prev.next = tmp_head.next
                tmp_head.next.prev = tmp_head.prev
                if tmp_head == self.head:
                    self.head = tmp_head.next
                self.length -= 1
                return True
            tmp_head = tmp_head.next
        return False

    def print(self, times):
        tmp_head = self.head
        s = "["
        for i in range(times):
            s += str(tmp_head.val) + ", "
            tmp_head = tmp_head.next
        s += "]"
        print(s)
