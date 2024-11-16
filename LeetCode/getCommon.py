class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {}
        for n in nums1:
            if n not in dic:
                dic[n] = 1
        
        for n in nums2:
            if n in dic:
                return n
        
        return -1
        
