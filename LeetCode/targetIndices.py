class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        res =[]
        for n in range(len(nums)):
            if nums[n] == target:
                res.append(n)
        return res
