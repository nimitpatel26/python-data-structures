


import math
class Bellman:
    def __init__(self, al, w):
        self.al = al
        self.d = [math.inf for i in al]
        self.visited = set()
        self.d[0] = 0

        for i in range(len(al)):
            changed = False
            for node, children in enumerate(al):
                dist_so_far = self.d[node]
                for child in children:
                    here_to_child = w[(node, child)]
                    total_dist = dist_so_far + here_to_child
                    curr_dist = self.d[child]
                    if total_dist < curr_dist:
                        self.d[child] = total_dist
                        changed = True
            if not changed:
                break
            if i == len(al) - 1 and changed:
                print("Invalid graph, negative cycle")
        print(self.d)



