class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        dp = [[0]*(len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        