class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        rem = 0
        for n in range(1,K+1):
            rem = (rem*10+1) % K
            if rem == 0:
                return n
        return -1