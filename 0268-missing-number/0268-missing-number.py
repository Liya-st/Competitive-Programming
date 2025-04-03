class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        nums.append(-1)
        while i < n:
            pos = nums[i]
            if 0 <= pos < n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        
        for i, n in enumerate(nums):
            if i != nums[i]:
                return i

        # print(nums)
        