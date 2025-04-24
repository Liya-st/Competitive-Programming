class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        q = deque()
        res = []
        vis = set()
        indegree = defaultdict(int)

        for i in range(len(graph)):
            for n in graph[i]:
                g[n].append(i)
            if graph[i]:
                indegree[i] += len(graph[i])
            
        for i in range(len(graph)):
            if not indegree[i]:
                q.append(i)
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in g[node]:
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    q.append(neigh)
                    vis.add(neigh)
        return sorted(res)


