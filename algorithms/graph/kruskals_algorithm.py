from collections import defaultdict


class Kruskal:
    def __init__(self, al, w):
        self.al = al
        self.w = w
        self.all_edges = []
        self.min_edges = []
        self.sets = defaultdict(set)

        for node, children in enumerate(self.al):
            for child in children:
                self.all_edges.append((node, child, self.w[(node, child)]))
        self.all_edges = sorted(self.all_edges, key = lambda x: x[2])

        for node, children in enumerate(self.al):
            self.sets[node].add(node)

        for edge in self.all_edges:
            u, v, w = edge
            if self.sets[u] != self.sets[v]:
                uv = self.sets[u].union(self.sets[v])

                for n in uv:
                    self.sets[n] = uv

                self.min_edges.append((u, v, w))

        print(self.min_edges)