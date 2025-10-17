class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        def dp(idx, allowed, buy):
            if idx >= len(prices):
                return 0

            if allowed <= 0:
                return 0
            
            if (idx, allowed, buy) not in memo:
                if buy:
                    memo[(idx, allowed, buy)] = max(- prices[idx] + dp(idx + 1, allowed, not buy) , dp(idx + 1, allowed, buy))
                else:
                    memo[(idx, allowed, buy)] = max(dp(idx + 1, allowed -1, not buy) + prices[idx], dp(idx + 1, allowed, buy))
            return memo[(idx, allowed, buy) ]
        return dp(0, k, True)
                   


        