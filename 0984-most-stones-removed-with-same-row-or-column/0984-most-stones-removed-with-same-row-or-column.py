class DSU:
    def __init__(self, size):
        self.root = list(range(size + 1))
        self.size = [1] * (size + 1)
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
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = DSU(len(stones))
        n = len(stones)
        l = 0
        r = 1
        lists = []
        for l in range(len(stones)):
            for r in range(l+1, len(stones)):
                if stones[l][0] == stones[r][0] or stones[l][1] == stones[r][1]:
                    uf.union(l, r)
                    print(l, r)
                
        temp = set()
        answer = 0
        for i in range(len(stones)):
            res = uf.find(i)
            print(res)
            if res not in temp:
                temp.add(res)
                answer += uf.size[res] - 1
        return answer