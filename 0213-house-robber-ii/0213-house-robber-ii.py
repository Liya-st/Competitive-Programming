class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def dp(idx, taken):
            if idx >= len(nums) -1 and taken:
                return 0
            if idx >= len(nums):
                return 0
            state = (idx, taken)
            if state in memo:
                return memo[state]
            memo[state] = max(nums[idx] + dp(idx + 2,taken), dp(idx+1, taken))  
            return memo[state]
        return max(dp(0, True), dp(1, False))    