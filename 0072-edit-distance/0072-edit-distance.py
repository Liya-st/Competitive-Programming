class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(idx1, idx2):
            if idx1 == len(word1):
                return len(word2) - idx2
            if idx2 == len(word2):
                return len(word1) - idx1
            state = (idx1, idx2)
            if state not in memo:
                if word1[idx1] == word2[idx2]:
                    memo[state] = dp(idx1+1, idx2+1)
                else:
                    insert = dp(idx1+1, idx2+1)
                    memo[state] = min(dp(idx1 + 1, idx2), dp(idx1, idx2+1))
                    memo[state] = 1 + min(insert, memo[state])

            return memo[state]
        return dp(0, 0)

        