class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums)-1
        res = 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] == k:
                i+=1
                j-=1
                res += 1
            elif nums[i] + nums[j] > k:
                j-=1
            else:
                i+=1
        return res

        
