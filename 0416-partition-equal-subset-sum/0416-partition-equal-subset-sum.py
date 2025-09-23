class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if total % 2 != 0:
            return False
        memo = {}

        def dp(idx, w):
            if w > half:
                return False
            if w == half:
                return True
            if idx >= len(nums):
                return False
            if (idx, w) in memo:
                return memo[(idx, w)]

            cur = w + nums[idx]
            memo[(idx, w)] = dp(idx + 1, cur) or dp(idx+1, w)
            return memo[(idx, w)]
        return dp(0, 0)
        