class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        memo = {}
        k = len(word)
        def dp(i):

            if i + k > len(sequence):
                return 0 
            if i in memo:
                return memo[i]
            if sequence[i: i + k] == word:
                memo[i] = 1 + dp(i + k)
            else:
                memo[i] = 0
            return memo[i]
        res = 0
        for i in range(len(sequence)):
            res = max(res, dp(i))

        return res