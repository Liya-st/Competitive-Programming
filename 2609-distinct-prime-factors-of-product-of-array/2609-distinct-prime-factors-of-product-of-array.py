class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        
        def prime(n):
            s = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    s.add(d)
                    n //= d
                d += 1
            if n > 1:
                s.add(n)
            return s
        
        for n in nums:
            res |= prime(n)
        
        return len(res)
