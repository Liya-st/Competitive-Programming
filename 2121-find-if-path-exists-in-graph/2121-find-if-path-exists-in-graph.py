class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        visited = set()

        for n, m in edges:
            adj[n].append(m)
            adj[m].append(n)

        stack = [source]
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            for neigh in adj[curr]:
                if neigh not in visited:
                    stack.append(neigh)
                    visited.add(neigh)
        return False

