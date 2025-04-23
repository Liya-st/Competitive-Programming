class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        offset = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = [[0 for _ in range(len(mat[0]))]for _ in range(len(mat))]
        q = deque()
        visited = [[False for _ in range(len(mat[0]))]for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        def inbound(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        while q:
            i, j, k = q.popleft()
            visited[i][j] = True
            for row,  col in offset:
                row += i
                col += j
                if inbound(row, col) and mat[row][col] == 1 and not visited[row][col]:
                    res[row][col] = k + 1 
                    visited[row][col] = True
                    q.append((row, col, k+1))
        return res                
                
        