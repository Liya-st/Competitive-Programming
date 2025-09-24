class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 1)
        def dp(idx):
            if idx >= len(cost):
                return 0
            if memo[idx] != -1:
                return memo[idx]
            
            memo[idx] = cost[idx] + min(dp(idx+1), dp(idx + 2))
            return memo[idx]
        return min(dp(0), dp(1))