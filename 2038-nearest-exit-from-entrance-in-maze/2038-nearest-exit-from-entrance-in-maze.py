class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

        def inbound(i, j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0])

        q = deque([(entrance[0], entrance[1], 0)])
        en = set()

        for row, col in offset:
            row += entrance[0]
            col += entrance[1]
            if not inbound(row, col):
                en.add((row, col))

        while q:
            i, j, step = q.popleft()
            for row, col in offset:
                row += i
                col += j
                if inbound(row, col) and not visited[row][col] and maze[row][col] == '.':
                    visited[row][col]  = True
                    q.append((row, col,step + 1 ))
                elif not inbound(row, col) and (row, col) not in en:
                    return step 
        return -1
