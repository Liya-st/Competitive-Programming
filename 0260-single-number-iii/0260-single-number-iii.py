class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res= []
        

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break
            if not found:
                res.append(nums[i])
                if len(res) == 2:
                    break

        return res