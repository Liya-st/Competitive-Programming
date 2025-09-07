class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = res = 0
        
        for num in nums:
            if num == 1:
                res += 1
                max_ = max(max_, res)
            else:
                res = 0
        return max_