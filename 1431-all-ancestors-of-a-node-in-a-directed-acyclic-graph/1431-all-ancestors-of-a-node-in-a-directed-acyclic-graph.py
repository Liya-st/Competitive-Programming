class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        res = [set() for _ in range(n)]
        def dfs(node):
            for neigh in graph[node]:
                if neigh not in res[node]:
                    res[node].add(neigh)
                    dfs(neigh)
                    res[node].update(res[neigh])
        for i in range(n):
            dfs(i)
        return [sorted(list(r)) for r in res]

    

        


