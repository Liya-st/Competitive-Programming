class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 1431655765
        res =  n | num
        if n <= 0:
            return False
        if res == num and (n & (n - 1) == 0):
            return True
        return False
        
        