class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[1 if i == j else 0 for i in range(len(s))] for j in range(len(s))]
        if len(s) == 1:
            return 1
        def inbound(i, j):
            if 0 <= i < len(s) and 0 <= j < len(s):
                return dp[i][j]
            
            return 0
        max_ = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 
                    if i + 1 <= j -1:
                        dp[i][j] += inbound(i+1, j-1)
                else:
                    dp[i][j] = max(inbound(i+1,j), inbound(i,j-1))
                max_ = max(max_, dp[i][j])
        return max_
        
        
