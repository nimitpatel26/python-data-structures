class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.balance_factor = 0
        self.height = 1


class AVL:
    def __init__(self, comp):
        self.root = None
        self.count = 0
        self.comparator = comp

    def insert(self, item):
        if self.is_empty():
            self.root = Node(item)
            self.count += 1
            return
        self.root = self.insert_item(self.root, item)
        self.adjust_node_data(self.root)
        self.count += 1

    def insert_item(self, node, item):

        if not node:
            return Node(item)

        right = True

        if self.comparator(item, node.val):
            right = False

        if not right:
            node.left_child = self.insert_item(node.left_child, item)

        if right:
            node.right_child = self.insert_item(node.right_child, item)

        self.adjust_node_data(node)
        if node.balance_factor > 1:
            if right:
                node.left_child = self.left_rotate(node)
            return self.right_rotate(node)

        elif node.balance_factor < -1:
            if not right:
                node.right_child = self.right_rotate(node)
            return self.left_rotate(node)

        return node

    def right_rotate(self, node):
        left = node.left_child
        node.left_child = left.right_child
        left.right_child = node
        self.adjust_node_data(node)
        self.adjust_node_data(left)
        return left

    def left_rotate(self, node):
        right = node.right_child
        node.right_child = right.left_child
        right.left_child = node
        self.adjust_node_data(node)
        self.adjust_node_data(right)
        return right

    def adjust_node_data(self, node):
        left_height = node.left_child.height if node.left_child else 0
        right_height = node.right_child.height if node.right_child else 0
        height = max(left_height, right_height) + 1
        node.height = height
        node.balance_factor = left_height - right_height

    def remove(self, item):
        pass

    def is_empty(self):
        return self.count == 0
