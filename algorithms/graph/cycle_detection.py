



class CycleDetection:
    def __init__(self, al):
        self.al = al
        self.n = len(self.al)
        self.v = [-1 for _ in range(self.n)]
        cycle = False
        for i in range(self.n):
            if self.v[i] == 1:
                continue
            self.v[i] = 0
            if self.dfs(i):
                cycle = True
                print("CYCLE DETECTED")
                break
        if not cycle:
            print("NO CYCLE DETECTED")


    def dfs(self, node):

        for child in self.al[node]:
            if self.v[child] == 1:
                continue
            if self.v[child] == 0:
                return True
            self.v[child] = 0
            if self.dfs(child):
                return True

        self.v[node] = 1
        return False









