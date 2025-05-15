class DSU:
    def __init__(self):
        self.root = {}
        self.size = {}
    def init(self, node):
        self.root[node] = node
        self.size[node] = 1

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
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ufd = DSU()
        for eq in equations:
            if eq[1:3] == "==":
                if eq[0] not in ufd.root:
                    ufd.init(eq[0])
                    
                if eq[3] not in ufd.root:
                    ufd.init(eq[3])

                ufd.union(eq[0], eq[3])
            else:
                if eq[0] not in ufd.root:
                    ufd.init(eq[0])
                if eq[3] not in ufd.root:
                    ufd.init(eq[3])
        res = True
        for eq in equations:
            if eq[1:3] == "==":
                if ufd.find(eq[0]) != ufd.find(eq[3]):
                    res = False
            else:
                if ufd.find(eq[0]) == ufd.find(eq[3]):
                    res = False
        return res


        