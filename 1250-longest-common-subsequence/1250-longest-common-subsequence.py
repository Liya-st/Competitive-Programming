class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        memo = [[-1] * (len(t) + 1 )for _ in range(len(s) + 1)]
        def dp(s_idx, t_idx):
            arr = []
            if s_idx >= len(s) or t_idx >= len(t):
                return 0
            
            if memo[s_idx][t_idx] != -1:
                return memo[s_idx][t_idx]
            if s[s_idx] == t[t_idx]:
                return 1 + dp(s_idx + 1, t_idx + 1)
            else:
                c1 = dp(s_idx + 1, t_idx)
                c2 = dp(s_idx, t_idx + 1)
            memo[s_idx][t_idx] = max(c1, c2)
            return  memo[s_idx][t_idx]
        return dp(0, 0)