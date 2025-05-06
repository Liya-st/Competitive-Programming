class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.size = [1] *( size + 1)
        self.ans = [0, 0]

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
                
        else:
            self.ans = [node1, node2]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ufd = UnionFind(len(edges))
        for i, j in edges:
            ufd.union(i, j)
        return ufd.ans
            

        
        