class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        i = 0
        dic = []
        while len(nums) > 1:
            dic = []
            for i in range(len(nums)-1):
                dic.append((nums[i] + nums[i+1]) % 10)
            nums = dic
        return nums[0]
    

        