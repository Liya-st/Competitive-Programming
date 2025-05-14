class DSU:
    def __init__(self, n):
        self.root = {}
        for i in range(n+1):
            for j in range(n+1):
                self.root[(i, j)] = (i, j)
        j = 0
        for i in range(n+1):
            self.root[(i, j)] = (0,0)
            self.root[(j, i)] = (0, 0)
        
        j = n
        for i in range(1, n+1):
            self.root[(i, j)] = (0,0)
            self.root[(j, i)] = (0, 0)
        
    def find(self, node):
        while node != self.root[node]:
            self.root[node] = self.root[self.root[node]]
            node = self.root[node]
        return self.root[node]
    def union(self, i, j):
        root1 = self.find(i)
        root2 = self.find(j)
        if root1 != root2:
            self.root[root1] = root2 
            return False
        return True

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        res = 1
        ufd = DSU(len(grid))
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '/':
                    node1 = (i, j+1)
                    node2 = (i + 1, j)
                    res += 1 if ufd.union(node1, node2) else 0
                elif grid[i][j] == "\\":
                    node1 = (i, j)
                    node2 = (i+1, j+1)
                    res += 1 if ufd.union(node1, node2) else 0
        return res


