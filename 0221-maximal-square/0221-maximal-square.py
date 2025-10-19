class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]

        dp[m-1][n-1] = int(matrix[m-1][n-1])

        def inbound(i, j):
            if 0 <= i < m and 0 <= j <n:
                return dp[i][j]
            return 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[j][i] == '1':
                    dp[j][i] = int(matrix[j][i]) + min(inbound(j+1,i+1),inbound(j+1,i) ,inbound(j,i+1))
        return max(max(row) for row in dp) ** 2

       