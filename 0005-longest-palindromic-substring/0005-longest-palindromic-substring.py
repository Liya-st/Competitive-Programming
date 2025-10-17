class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        memo = [[None] * n for _ in range(n)]

        def dfs(i,j):
            if i > j: return False
            if memo[i][j] is None:
                if i == j: memo[i][j] = True
                elif s[i] == s[j]:  
                    if j-i == 1: memo[i][j] = True
                    else: memo[i][j] = dfs(i+1,j-1)
                else: 
                    memo[i][j] = False
            return memo[i][j]

        for length in range(n):
            for i in range(n-length):
                if i+length >= len(res) and dfs(i,i+length):
                    res = s[i:i+length+1]

        return res