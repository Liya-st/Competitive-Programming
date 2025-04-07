class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        visited = set()

        for n, m in edges:
            adj[n].append(m)
            adj[m].append(n)

        def dfs(vertex):
            visited.add(vertex)
            if vertex == destination:
                return True
            for neigh in adj[vertex]:
                if neigh not in visited:
                    temp = dfs(neigh)
                    if temp:
                        return True
            return False
        return dfs(source)

