class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1]*(len(nums) + 1) for _ in range(len(nums)+ 1)]
        
        def dp(idx, prev):
            max_ = 0
            if idx >= len(nums):
                return 0
            if memo[idx][prev + 1] != -1:
                return memo[idx][prev + 1]
            take = 0
            if prev == -1 or nums[idx] > nums[prev]:
                take = 1 + dp(idx+1, idx)
            notake = dp(idx+1, prev)
            memo[idx][prev + 1] = max(take, notake)
            return memo[idx][prev + 1]
        return dp(0, -1)



        