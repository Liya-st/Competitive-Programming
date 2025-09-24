class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(idx, hold):
            if idx == len(prices):
                return 0

            state = (hold, idx)
            if state in memo:
                return memo[state]
            res = 0
            if hold:
                res = max(prices[idx] - fee + dp(idx+1, False), dp(idx +1, True))
            else:
                res = max(dp(idx + 1, True)-prices[idx], dp(idx+1, False))
            memo[state] = res
            return res
        res = 0
        for i in range(len(prices)):
            res = max(res, dp(i, False))
        return res



            
            

            

        