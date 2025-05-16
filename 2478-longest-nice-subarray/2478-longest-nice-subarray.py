class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_ =0
        acc = 0
        while j < len(nums):
            while (acc & nums[j]) != 0:
                acc &= ~nums[i]
                i+=1
            acc |= nums[j]
            max_ = max(max_, j-i+1)
            j+=1
        return max_ 

        