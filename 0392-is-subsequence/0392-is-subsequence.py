class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        def dp(idx1, idx2):
            if idx1 >= len(s):
                return True
            if idx2 >= len(t):
                return False
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            res = False
            if s[idx1] == t[idx2]:
                res = dp(idx1 + 1, idx2+1)
            else:
                res = dp(idx1, idx2 +1)
            memo[(idx1, idx2)] = res
            return res
        return dp(0, 0)
        