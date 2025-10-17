class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def dfs(curr, path):
            path = path + [curr]
            if curr == n-1:
                res.append(path)
                return
            
            for neigh in graph[curr]:
                if neigh not in path:
                    dfs(neigh, path)
        dfs(0, [])
        return res
                