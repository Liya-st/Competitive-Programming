class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        start = 0
        res = 0
        for i, n in enumerate(manager):
            if n == -1:
                start = i
                continue
            graph[n].append(i)
        def dfs(node):
            nonlocal res
            max_ = 0
            
            for neigh in graph[node]:
                max_ = max(max_, dfs( neigh))
            return max_ + informTime[node]
        return dfs(start)



        