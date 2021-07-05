import math


class Ford:
    def __init__(self, al, w, s, t):
        self.al = al
        self.w = w
        self.s = s
        self.t = t
        self.visited = set()
        self.parent = {}

    def max_flow(self):
        flow = 0
        while self.viable_path(self.s):
            path_flow = math.inf
            node = self.t
            while node != self.s:
                p = self.parent[node]
                cost = self.w[(p, node)]
                path_flow = min(path_flow, cost)
                node = p

            flow += path_flow

            node = self.t
            while node != self.s:
                p = self.parent[node]
                self.w[(p, node)] -= path_flow
                node = p

            self.visited = set()
            self.parent = {}
        print(flow)



    def viable_path(self, node):
        if node == self.t:
            return True

        path = False
        for child in self.al[node]:
            if self.w[(node, child)] > 0 and (node, child) not in self.visited:
                self.visited.add((node, child))
                if child not in self.parent:
                    self.parent[child] = node
                path = path or self.viable_path(child)
        return path



