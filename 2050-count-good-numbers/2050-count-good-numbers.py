class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def helper(n,x ):
            if n == 0:
                return 1
            res = helper(n//2, x)
            res = res * res
            if n % 2 == 1:
                return x * res % mod
            return res % mod
        even_c = n//2 + n%2
        odd_c = n//2
        return helper(even_c, 5) * helper(odd_c, 4) % mod

        

       
        