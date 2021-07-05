import math


class Floyd:
    def __init__(self, al, w):
        self.al = al
        self.w = w

        self.a_old = [[math.inf for i in self.al] for j in self.al]
        self.a_new = [[math.inf for i in self.al] for j in self.al]

        for node, children in enumerate(self.al):
            for child in children:
                self.a_old[node][child] = self.w[(node, child)]
            self.a_old[node][node] = 0
            

        for n in range(len(self.al)):
            for u in range(len(self.al)):
                for v in range(len(self.al)):
                    self.a_new[u][v] = min(self.a_old[u][v], self.a_old[u][n] + self.a_old[n][v])

            self.a_old = self.a_new
            self.a_new = [[math.inf for i in self.al] for j in self.al]

        for row in self.a_old:
            print(row)

