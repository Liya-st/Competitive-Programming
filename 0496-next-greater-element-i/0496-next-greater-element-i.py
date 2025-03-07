class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic = {}
        res = []

        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                n = stack.pop()
                dic[int(n)] = nums2[i]
            stack.append(nums2[i])

        for n in nums1:
            if n not in dic:
                res.append(-1)
            else:
                res.append(dic[n])

        return res


        
        