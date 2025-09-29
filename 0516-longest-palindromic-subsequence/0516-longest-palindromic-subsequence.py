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
            if s[i] == s[j]:
                memo[i][j] =  2 + dp(i+1, j-1)
            else:
                memo[i][j] = max(memo[i][j], dp(i+1, j))
                memo[i][j] = max(memo[i][j], dp(i, j-1))
            return memo[i][j]
        return dp(0, len(s)-1)
