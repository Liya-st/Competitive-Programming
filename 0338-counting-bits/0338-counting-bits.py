class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = list(range(n + 1))
        res = [0]*len(nums)
        prev = 0
        i = 1
        while i < len(nums):
            if nums[i] == 2**prev:
                res[i] = 1
                prev +=1
            else:
                res[i] = res[int(i - 2**(prev-1))] + 1     
            i+=1
        return res
            


