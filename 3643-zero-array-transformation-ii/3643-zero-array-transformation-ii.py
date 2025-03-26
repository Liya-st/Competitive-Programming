class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)
        res = -1

        while left <= right:
            mid = (left + right) // 2
            prefix = [0] * (len(nums) + 1)  
            for k in range(mid):
                i, j, val = queries[k]
                prefix[i] -= val 
                if j + 1 < len(nums):
                    prefix[j + 1] += val 

            acc = 0
            broken = False
            for i in range(len(nums)):
                acc += prefix[i]  
                if nums[i] + acc > 0:  
                    broken = True
                    break

            if broken:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res