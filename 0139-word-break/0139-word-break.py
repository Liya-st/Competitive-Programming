class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(idx):
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]
            for word in wordDict:
                if s[idx:idx+len(word)] == word and dp(idx+len(word)):
                    memo[idx] = True
            if idx not in memo:
                memo[idx] = False
            return memo[idx]
        return dp(0)
                
        