class DSU:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.size = [1] *( size + 1)
        self.nodes = size
    def find(self, node):
        
        while node != self.root[node]:
            self.root[node] = self.root[self.root[node]]
            node = self.root[node]
        return self.root[node]
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.size[root1] += self.size[root2]
                self.root[root2] = root1
            else:
                self.size[root2] += self.size[root1]
                self.root[root1] = root2
            self.nodes -=1
            return True
        return False
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufdA = DSU(n)
        ufdB = DSU(n)
        res = 0
        for t, x, y in edges:
            if t == 3:
                if not ufdA.union(x, y) or not ufdB.union(x, y):
                    res +=1
        for t, x, y in edges:
            if t == 1:
                if not ufdA.union(x, y):
                    res += 1
            elif t == 2:
                if not ufdB.union(x, y):
                    res += 1
        
        if ufdA.nodes != 1 or ufdB.nodes != 1:
            return -1

        return res



        
        