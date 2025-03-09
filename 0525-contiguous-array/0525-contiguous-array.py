class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        dic = {0: -1}  
        prefix = 0
        max_ = 0
        
        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1
            
            if prefix in dic:
                max_ = max(max_, i - dic[prefix])
            else:
                dic[prefix] = i
        
        return max_
