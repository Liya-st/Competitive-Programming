class UFD:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
    
        
class Solution:
    def minScore(self, n, roads: List[List[int]]) -> int:
        ufd = UFD(n)
        
        res = float('inf')
        for road in roads:
            ufd.union(road[0], road[1])
        for road in roads:
            root1 = ufd.find(1)
            rootX = ufd.find(road[0])
            rootY = ufd.find(road[1])
            if root1 == rootX == rootY:
                res = min(res, road[2])
        return res