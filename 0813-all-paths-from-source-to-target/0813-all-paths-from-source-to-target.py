class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        q = deque([(0, [0])])
        target = n-1

        while q:
            node, path = q.popleft()
            if node == target:
                res.append(path)

            for neigh in graph[node]:
                new_path = path + [neigh]
                q.append((neigh, new_path))
            
        return res

                