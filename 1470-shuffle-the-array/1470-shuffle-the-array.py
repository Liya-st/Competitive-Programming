class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        idx = n
        res = []
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[idx+i])
        return res
