class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_ =  float('inf') 
        max_ =  float('inf') 
        bound = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bound = i  

            if num == minK:
                min_ = i  
                         
            if num == maxK:
                max_ = i  
            if min_ !=  float('inf')  and max_ !=  float('inf') :
                res += max(0, min(min_, max_) - bound)  
            # print(num, res, bound) 
        return res
