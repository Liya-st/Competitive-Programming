class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dic = {
            1 : [(0, 1), (0, -1)],
            2 : [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)], 
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def inbound(i, j, n, m):
            return 0 <= i < m and 0 <= j < n
        def possible(prev1, prev2, i, j):
            path = dic[grid[i][j]]
            for x, y in path:
                x += i
                y += j
                if  x == prev1 and y == prev2:
                    return True
            return False
                
        stack = [(0, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        while stack: 
            i, j = stack.pop()
            visited[i][j] = True
            if (i, j) == (len(grid)-1, len(grid[0])-1):
                return True
            path = dic[grid[i][j]]
            for x, y in path:
                x += i
                y += j
                if inbound(x, y, len(grid[0]), len(grid)) and possible(i, j, x, y) and not visited[x][y]:
                    stack.append((x, y))

        return False




        