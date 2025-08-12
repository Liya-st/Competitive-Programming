class DSU:
    def __init__(self, size):
        self.root = [ i for i in range(size)]
        self.size = [1] *( size + 1)
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(s1, s2):
            count  = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count +=1
            return count <= 2
        ufd = DSU(len(strs))
        for i in range(len(strs)):
            for j in range(i, len(strs)):
                if check(strs[i], strs[j]):
                    ufd.union(i, j)
        count = set()
        for i in range(len(strs)):
            count.add(ufd.find(i))
        return len(count)
