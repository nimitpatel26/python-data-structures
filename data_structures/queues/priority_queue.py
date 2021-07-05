"""

Uses of a Priority Queue:
    (1) Dijkstra's algorithm
    (2) Implementing stacks
    (3) Load balancing and interrupt handling
    (4) For compression in Huffman code


"""


class PriorityQueue:
    def __init__(self, capacity, compare):
        self.capacity = capacity
        self.compare = compare
        self.length = 0
        self.queue = [None] * self.capacity

    def enqueue(self, item):
        if self.length == self.capacity:
            return False
        self.queue[self.length] = item
        self.length += 1

        # heapify up from self.length - 1
        self.heapify_up(self.length - 1)

    def heapify_up(self, child_index):
        if child_index == 0:
            return
        parent_index = (child_index - 1) // 2

        child = self.queue[child_index]
        parent = self.queue[parent_index]

        # parent is less than child
        if self.compare(parent, child):
            self.queue[parent_index], self.queue[child_index] = self.queue[child_index], self.queue[parent_index]

        return self.heapify_up(parent_index)

    def dequeue(self):
        if self.is_empty():
            return "Queue Is Empty"

        item = self.queue[0]
        self.queue[0] = self.queue[self.length - 1]
        self.queue[self.length - 1] = None
        self.length -= 1

        # heapify down from 0
        self.heapify_down(0)

        return item

    def heapify_down(self, parent_index):

        left_child_index = parent_index * 2 + 1
        right_child_index = parent_index * 2 + 2

        if self.length == 0 or parent_index >= self.length or left_child_index >= self.length:
            return

        """
        
        left < parent < right               right
        right < parent < left               left
        
        parent < left < right               right
        parent < right < left               left
            
        left < right < parent               return
        right < left < parent               return
        
        
        
        """

        # all exist
        # right doesn't exist

        if right_child_index >= self.length:
            if self.compare(self.queue[parent_index], self.queue[left_child_index]):
                self.queue[parent_index], self.queue[left_child_index] = self.queue[left_child_index], self.queue[
                    parent_index]
                return self.heapify_down(left_child_index)
            return

        go_right = self.compare(self.queue[parent_index], self.queue[left_child_index]) and self.compare(
            self.queue[left_child_index], self.queue[right_child_index])
        go_right = go_right or (self.compare(self.queue[left_child_index], self.queue[parent_index]) and self.compare(
            self.queue[parent_index], self.queue[right_child_index]))

        go_left = self.compare(self.queue[parent_index], self.queue[right_child_index]) and self.compare(
            self.queue[right_child_index], self.queue[left_child_index])
        go_left = go_left or (self.compare(self.queue[right_child_index], self.queue[parent_index]) and self.compare(
            self.queue[parent_index], self.queue[left_child_index]))

        if go_right:
            self.queue[parent_index], self.queue[right_child_index] = self.queue[right_child_index], self.queue[
                parent_index]
            return self.heapify_down(right_child_index)

        # parent < right < left
        if go_left:
            self.queue[parent_index], self.queue[left_child_index] = self.queue[left_child_index], self.queue[
                parent_index]
            return self.heapify_down(left_child_index)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return "Queue Is Empty"
        return self.queue[0]
