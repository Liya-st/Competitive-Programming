class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                res.append(nums[i])
            else:
                nums[i] = nums[i]*2
                nums[i+1] = 0
                res.append(nums[i])
        res.append(nums[len(nums)-1])
        nonzeros = [i for i in res if i!= 0]
        zeros = res.count(0) * [0]
        res = nonzeros + zeros
        return res
        


            
        
