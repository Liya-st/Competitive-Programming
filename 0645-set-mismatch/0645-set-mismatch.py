class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            pos = nums[i] -1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            
            else:
                i+=1
        for i, n in enumerate(nums):
            if i != nums[i]-1:
                return [nums[i], i+1]

    