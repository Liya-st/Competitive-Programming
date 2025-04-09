class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        offset=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        ans = 0

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0])) and grid[row][col] == 1

        def dfs(row, col):
            visited[row][col] = True 
            count = 1
            for row_c, col_c in offset:
                new_row = row_c + row
                new_col = col_c + col
                if inbound(new_row, new_col) and not visited[new_row][ new_col]:
                    count += dfs(new_row, new_col) 
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    n = dfs(i, j)
                    ans = max(ans, n)
        return ans
