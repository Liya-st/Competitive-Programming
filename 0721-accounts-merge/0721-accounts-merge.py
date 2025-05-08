class DSU:
    def __init__(self):
        self.root = defaultdict(lambda: None)
        self.size = defaultdict(int)

    def find(self, node):
        if self.root[node] is None:
            self.root[node] = node
            self.size[node] = 1
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]      

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                self.root[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.root[root2] = root1
                self.size[root1] += self.size[root2]
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ufd = DSU()
        maps = {}
        res = []
        
        for account in accounts:
            parent = account[1]
            acc = account[0]
            for i in range(1, len(account)):
                ufd.union(parent, account[i])
                maps[account[i]] = acc
        
        merged = defaultdict(list)
        for email in maps:
            merged[ufd.find(email)].append(email)

        for key, emails in merged.items():
            res.append([maps[key]] + sorted(emails))
            
        return sorted(res)
