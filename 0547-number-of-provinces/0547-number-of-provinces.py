class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        visited = [False] * len(grid)
        res = 0

        def bfs(q):
            while q:
                node = q.popleft()
                for i in range(len(grid)):
                    if grid[node][i] == 1 and not visited[i]:
                        q.append(i)
                        visited[i] = True
        for i in range(len(grid)):
            if not visited[i]:
                bfs(deque([i]))
                res +=1
        return res

        
        

        



            




        
        