class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        up_x, down_x = float("inf"), 0
        up_y, down_y = float("inf"), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    up_x = min(up_x, i)
                    down_x = max(down_x, i)
                    up_y = min(up_y, j)
                    down_y = max(down_y, j)

        return (down_x - up_x + 1) * (down_y - up_y + 1)