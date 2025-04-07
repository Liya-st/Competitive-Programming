class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        offset = [(0,1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        row  = -1
        col = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row = i
                    col= j
                    break
            if row != -1:
                break
        
            

        
        def inbound(row, col):
            return ((0 <= row < len(grid)) and (0 <= col < len(grid[0])))
        
        def dfs(row,col):
            nonlocal res
            visited[row][col] = True
            for i, j in offset:
                new_i = i+row
                new_j = j+col
                if not inbound(new_i, new_j) or  grid[new_i][new_j] == 0:
                    res +=1
                elif inbound(new_i, new_j):
                    if not visited[new_i][new_j] and grid[new_i][new_j] == 1:
                        dfs(new_i, new_j)
        dfs(row,col)
        return res
