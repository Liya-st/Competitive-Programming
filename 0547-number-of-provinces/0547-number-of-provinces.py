class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, node):
        root = node
        while self.root[root] != root:
            root = self.root[root]
        while node != root:
            parent = self.root[node]
            self.root[node] = root
            node = parent
        return root

    def Union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.size[root1] += self.size[root2]
                self.root[root2] = root1
            else:
                self.size[root2] += self.size[root1]
                self.root[root1] = root2

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        visited = [False] * len(grid)
        res = len(grid)
        ufd = UnionFind(len(grid))

        for i in range(len(grid)):
            for j in range(i+1, len(grid)):
                if grid[i][j] == 1 and ufd.find(i) != ufd.find(j):
                    res -=1
                    ufd.Union(i, j)

        return res
    



        
        

        



            




        
        