class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []
        for i,n in enumerate(equations):
            u, v = n
            graph[u].append((v, values[i]))
            graph[v].append((u, 1/values[i]))

        def bfs(u, v):
            vis = set([u])
            q = deque([(u, 1)])
            if u not in graph or v not in graph:
                return -1.0
            while q:
                node, val = q.popleft()
                if node == v:
                    return val
                for neigh, value in graph[node]:
                    if neigh not in vis:
                        q.append((neigh, val*value))
                        vis.add(neigh)
        
            return -1.0
        for u, v in queries:
            res.append(bfs(u, v))
        return res