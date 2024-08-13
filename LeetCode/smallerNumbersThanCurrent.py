class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        sortedNums = sorted(nums)
        for num in nums:
            res.append(sortedNums.index(num))
        return res
        
