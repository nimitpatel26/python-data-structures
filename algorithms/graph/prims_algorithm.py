

class Prims:
    def __init__(self, al, w):
        self.al = al
        self.w = w
        self.all_edges = []

        for node, children in enumerate(self.al):
            for child in children:
                self.all_edges.append((node, child, self.w[(node, child)]))

        self.all_edges = sorted(self.all_edges, key = lambda x: x[2])
        self.min_edges = [self.all_edges.pop()]
        self.nodes_connected = {self.min_edges[0][0], self.min_edges[0][1]}

        while len(self.nodes_connected) != len(self.al):
            for edge in self.all_edges:
                u, v, w = edge
                if (u in self.nodes_connected and v not in self.nodes_connected) or (v in self.nodes_connected and u not in self.nodes_connected):
                    self.nodes_connected.add(u)
                    self.nodes_connected.add(v)
                    self.min_edges.append((u, v))

        print(self.min_edges)





