class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        res = 0
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = nums[i] + max(dp(i+2), dp(i+3))
            return memo[i]
        for i in range(2):
            res = max(res, dp(i))
        return res



        
        