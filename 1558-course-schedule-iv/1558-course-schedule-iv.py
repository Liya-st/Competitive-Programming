class Solution:
    def checkIfPrerequisite(self, num: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        temp = [[False for _ in range(num)] for _ in range(num)]
        res = []

        for u, v in prerequisites:
            graph[u].append(v)
        
   
        def dfs(node):      
            for n in graph[node]:
                if not temp[node][n]:
                    temp[node][n] = True
                    dfs(n)
                for i in range(num):
                    if temp[n][i] and not temp[node][i]:
                        temp[node][i] = True
        for n in range(num):
            dfs(n)
        for  u, v in queries:
            res.append(temp[u][v])
        return res
      