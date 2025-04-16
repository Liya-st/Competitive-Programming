class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        visited = set()
        
        def bfs(q):
            edges = 0
            while q:
                node = q.popleft()
                count[0] +=1
                edges += len(graph[node])
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            return edges // 2 == (count[0] *( count[0] -1) )//2
            
        for i in range(n):
            if i not in visited:
                count = [0]
                visited.add(i)
                if bfs(deque([i])):
                    res +=1
        return res



        