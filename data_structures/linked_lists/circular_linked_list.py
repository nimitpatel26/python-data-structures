"""

Why circular linked list?
    (1) NULL assignment is not required because a node will always point to a node
    (2) Head can be any node
    (3) Traversal from first node to last is quick

Uses of a circular linked list
    (1) Multiplayer games to give each player a chance
    (2) OS can run over multiple running application

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.head.next = self.head
            self.length += 1
            return

        node = Node(item)
        tmp_node = self.head
        while tmp_node.next != self.head:
            tmp_node = tmp_node.next

        tmp_node.next = node
        node.next = self.head
        self.length += 1

    def remove(self, item):
        if self.is_empty():
            return False

        if self.length == 1 and self.head.val == item:
            self.length -= 1
            self.head = None
            return True

        prev_node = self.head
        tmp_node = self.head.next

        while tmp_node != self.head:
            if tmp_node.val == item:
                prev_node.next = tmp_node.next

                if tmp_node == self.head:
                    self.head = tmp_node.next

                self.length -= 1
                return True
            prev_node = tmp_node
            tmp_node = tmp_node.next

        if tmp_node.val == item:
            prev_node.next = tmp_node.next

            if tmp_node == self.head:
                self.head = tmp_node.next

            self.length -= 1
            return True

        return False

    def print(self, times):
        if self.is_empty():
            print("[]")
            return

        tmp_node = self.head
        s = "["
        for i in range(times):
            s += str(tmp_node.val) + ", "
            tmp_node = tmp_node.next
        s += "]"
        print(s)
