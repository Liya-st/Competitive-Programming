class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n for _ in range(m)]
        def inbound(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0
        offset ={(0, 1), (1, 0)}
        for i in range(m):
            for j in range(n):
                for x, y in offset:
                    x += i
                    y += j
                    if inbound(x, y) != 0:
                        dp[x][y] = inbound(x-1,y) + inbound(x, y-1)
        return dp[-1][-1]
