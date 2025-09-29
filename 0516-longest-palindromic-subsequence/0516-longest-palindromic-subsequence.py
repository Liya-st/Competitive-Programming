class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1]*len(s) for _ in range(len(s))]
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            state = (i, j)
            if memo[i][j] != -1:
                return memo[i][j]
            temp = 0
            if s[i] == s[j]:
                temp = max(temp, 2 + dp(i+1, j-1))
            temp = max(temp, dp(i+1, j))
            temp = max(temp, dp(i, j-1))
            memo[i][j] = temp
            return memo[i][j]
        return dp(0, len(s)-1)
