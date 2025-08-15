class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        offset = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_ = 0
        def inbound(i, j, m, n):
            return 0 <= i < m and 0 <= j < n
        def dfs(i ,j):
            if visited[i][j] != 0:
                return visited[i][j]
            length =1
            for x, y in offset:
                x +=i
                y += j
                if inbound(x, y,len(matrix), len(matrix[0])):
                    if matrix[i][j] < matrix[x][y]:
                        length = max((1 +  dfs(x, y)) , length)
            visited[i][j] = length
            return length
                    
                 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_ = max(max_, dfs(i, j))
        return max_
        
        