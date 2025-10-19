class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[float("inf")]*(len(grid[0]) + 1 )for _ in range(len(grid) + 1)]
        n = len(grid)
        m = len(grid[0])
        final = (n-1, m-1)
        offset = [(0, 1), (1, 0)]
        def inbound(i, j):
            return ( 0 <= i < n) and (0 <= j < m)
        memo[n-1][m] = 0
        memo[n][m-1] = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                memo[i][j] = grid[i][j] + min(memo[i+1][j], memo[i][j+1])
        
             
        return memo[0][0]

            
            
            
            