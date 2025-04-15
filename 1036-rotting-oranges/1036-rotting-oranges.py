class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        offset = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        max_ =0

        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 
                 
        while q:
            i, j, time = q.popleft()
            for row, col in offset:
                row += i
                col += j
                if inbound(row, col):
                    grid[row][col] = 2
                    q.append((row, col, time + 1))
                    max_ = max(max_, time + 1)
        for i in range(len(grid)):
            if 1 in grid[i]:
                return -1
        return max_
        

        
                    





        