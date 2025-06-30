class DSU:
    def __init__(self, n):
        self.root = list(range(n))
    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]
    def union(self,node1, node2):
        root1 = self.find(node1)  
        root2= self.find(node2)
        if root1 < root2:
            self.root[root2] = root1
        elif root1 > root2:
            self.root[root1] = root2

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ufd = DSU(26)
        res = []
        for i in range(len(s1)):
            ufd.union(ord(s1[i])-97, ord(s2[i])-97)
        for let in baseStr:
            res.append(chr(ufd.find(ord(let)-97)+97))
        return "".join(res)