class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        res= 0
        i = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero +=1
            while zero > 1:
                if nums[i] == 0:
                    zero -=1
                i+= 1
            res = max(res, j-i)
        return res
        