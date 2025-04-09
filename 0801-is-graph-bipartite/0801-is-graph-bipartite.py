class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        paints = [-1 for _ in range(len(graph))]

        visited = set()
        stack = []
        def dfs(i):
            stack.append(i)
            visited.add(i)
            paints[i] = 0
            while stack:
                node = stack.pop()
                for neigh in graph[node]:
                    if paints[neigh] == -1:
                        paints[neigh] = 1- paints[node]
                    elif paints[node] == paints[neigh]:
                        return False
                    
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
            return True
        for i in range(len(graph)):
            if paints[i] == -1:
                if not dfs(i):
                    return False
        return True
        

        