class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        temp = 0
        for n in nums:
            temp ^= n
         
        for i in range(32):
            if ((temp >> i) & 1) != ((k >> i) & 1):
                res +=1
        return res