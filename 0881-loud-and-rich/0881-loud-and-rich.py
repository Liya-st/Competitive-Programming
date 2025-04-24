class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        paints = [-1 for _ in range(len(quiet))]
        res = [0 for _ in range(len(quiet))]

        for u, v in richer:
            graph[v].append(u)
        def dfs(node):
            if paints[node] != -1:
                return res[node]
            paints[node] = 0
            min_ = node
            for neigh in graph[node]:
                x = dfs(neigh)
                if quiet[min_] > quiet[x]:
                    min_ = x 
            paints[node] = 1
            res[node] = min_
            return min_

        for i in range(len(quiet)):
            dfs(i)
        return res

            

        

        