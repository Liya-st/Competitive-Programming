class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        paints = [-1 for _ in range(num)]
        res = []
        
        for u, v in pre:
            graph[v].append(u)
        def dfs(node):
            paints[node] = 0
            for neigh in graph[node]:
                if paints[neigh] == -1:
                    dfs(neigh)
                elif paints[neigh] == 0:
                    return False
                
            paints[node] = 1
            res.append(node)
            return True
        for i in range(num):
            if paints[i] == -1:
                if not dfs(i):
                    return []
        if len(res) != num:
            return []         
        return res[::-1]

        