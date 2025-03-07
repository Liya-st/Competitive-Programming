class Solution(object):
    def sumSubarrayMins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        res = 0
        stack = []
        sum_ = 0

        for i, n in enumerate(nums):
            count = 1  
            while stack and stack[-1][0] > n:  
                x, y = stack.pop()
                sum_ -= x * y
                count += y  

            stack.append((n, count))
            sum_ += n * count
            res += sum_
        
        return res % MOD  
