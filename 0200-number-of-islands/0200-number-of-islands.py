class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]) ) and grid[row][col] == "1"
            

        def dfs(i, j):
            visited[i][j] = True
            for row, col in offset:
                new_i = i + row
                new_j = j + col
                if inbound(new_i, new_j) and not visited[new_i][new_j]:
                    dfs(new_i, new_j)
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    res +=1
        return res
        

        