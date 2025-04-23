class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        q = deque()
        res = [[0 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        vis = [[False for _ in range(len(grid[0]))]for _ in range(len(grid))]
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        while q:
            i, j , k = q.popleft()
            for row, col in offset:
                row += i
                col += j
                if inbound(row, col) and grid[row][col] == 0 and not vis[row][col]:
                    res[row][col] = k+1
                    vis[row][col] = True
                    q.append((row, col, k+1))
        return res
            



        