import math
from collections import defaultdict


class Node:
    def __init__(self, index):
        self.vertex_index = index
        self.min_dist = math.inf

class Heap:
    def __init__(self, capacity, comparator):
        self.capacity = capacity
        self.heap = [None] * self.capacity
        self.comparator = comparator
        self.length = 0

    def get_min(self):
        if self.is_empty():
            return

        item = self.heap[0]
        self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
        self.heap[self.length - 1] = None
        self.length -= 1
        self.heapify_down(0)
        return item

    def heapify_down(self, index):
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        largest = index

        if right_index < self.length and self.comparator(self.heap[left_index], self.heap[right_index]) and self.comparator(self.heap[index], self.heap[right_index]):
            largest = right_index
        if left_index < self.length and self.comparator(self.heap[right_index], self.heap[left_index]) and self.comparator(self.heap[index], self.heap[left_index]):
            largest = left_index

        if largest == index:
            return

        self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
        return self.heapify_down(largest)

    def add(self, node):
        self.heap[self.length] = node
        self.heapify_up(self.length)
        self.length += 1

    def heapify_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        if self.comparator(self.heap[index], self.heap[parent_index]):
            self.heapify_up(parent_index)


    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.capacity

class Dijkstra:
    def __init__(self, al, w):
        self.al = al
        self.w = w
        self.heap = Heap(len(self.al) ** 2, lambda x, y: x.min_dist < y.min_dist)
        self.visited = set()
        self.dist = [math.inf for i in self.al]
        self.parent = [None for i in self.al]


        for index in range(1, len(al)):
            self.heap.add(Node(index))

        start = Node(0)
        start.min_dist = 0
        self.heap.add(start)


    def find(self):
        while len(self.visited) != len(self.al):
            node = self.heap.get_min()

            self.visited.add(node.vertex_index)
            for child in self.al[node.vertex_index]:
                node_to_child = self.w[(node.vertex_index, child)]
                total = node.min_dist + node_to_child
                if total < self.dist[child]:
                    self.dist[child] = total
                    self.parent[child] = node.vertex_index
                    newNode = Node(child)
                    newNode.min_dist = total
                    self.heap.add(newNode)
        print(self.dist)
        print(self.parent)

