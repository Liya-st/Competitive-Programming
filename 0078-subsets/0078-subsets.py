class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1 << len(nums)):
            temp = []
            for j, k in enumerate(bin(i)[2:].zfill(len(nums))):
                if k == '1':
                    temp.append(nums[j])
            res.append(temp)
        return res
        

        