class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, rem):
            if idx == len(nums):
                return 1 if rem == 0 else 0

            state = (idx, rem)
            if state in memo:
                return memo[state]
            
            memo[state] = dp(idx+1, rem - nums[idx]) + dp(idx + 1, rem + nums[idx])

            return memo[state]
        return dp(0, target)