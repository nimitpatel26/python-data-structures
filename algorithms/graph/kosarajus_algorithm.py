
class Kosaraju:
    def __init__(self, al):
        self.al = al
        self.stack = []
        self.visited = set()

        self.visit(0)

        self.visited = set()

        self.reversed = [[] for i in range(len(self.al))]

        for node, children in enumerate(self.al):
            for child in children:
                self.reversed[child].append(node)

        self.comps = self.get_comps()
        print(self.comps)

    def visit(self, node):
        if node in self.visited:
            return

        self.visited.add(node)
        for child in self.al[node]:
            self.visit(child)

        # mark the node as visited after all the children have been visited
        self.stack.append(node)

    def visitR(self, node):
        if node in self.visited:
            return []
        self.visited.add(node)

        comp = [node]
        for child in self.reversed[node]:
            comp += self.visitR(child)
        return comp

    def get_comps(self):

        comp = []
        while self.stack:
            node = self.stack.pop()
            if node in self.visited:
                continue
            comp += [self.visitR(node)]

        return comp
