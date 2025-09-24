class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, hold, cool):
            if idx == len(prices):
                return 0
            res = 0
            state = (idx, hold, cool)
            if state in memo:
                return memo[state]
            if not cool:
                if hold:
                    res = max(prices[idx] + dp(idx + 1, False, True), dp(idx + 1, True, False))
                else:
                    res = max(-prices[idx] + dp(idx + 1, True, False), dp(idx+1, False, False))
            else:
                res = dp(idx + 1, False, False)
            memo[state] = res
            return res
        return dp(0, False, False)
        