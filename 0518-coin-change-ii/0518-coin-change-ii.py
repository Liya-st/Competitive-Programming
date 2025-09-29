class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(rem, i):
            ways = 0
            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0
            state = (rem , i)
            if state in memo:
                return memo[state]
            if coins[i] <= rem:
                ways += dp(rem - coins[i], i)
            ways += dp(rem, i + 1)
            memo[state] = ways
            return memo[state]

        return dp(amount, 0)