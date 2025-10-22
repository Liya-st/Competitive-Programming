class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False]* n for _ in range(m)]

        def inbound(i, j):
            return (0 <= i < m) and (0 <= j < n)

        def dfs(i, j):
            if not inbound(i, j):
                return 0

            for x, y in directions:
                x += i
                y += j
                if inbound(x, y) and grid[x][y] == "1":
                    visited[x][y] = True
                    grid[x][y] = "0"

                    dfs(x, y)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    res +=1
                    dfs(i, j)
        return res
            


        