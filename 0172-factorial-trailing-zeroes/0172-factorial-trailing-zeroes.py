class Solution:
    def trailingZeroes(self, n: int) -> int:
   
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return n * factorial(n-1)
    
        a = factorial(n)
        c = 0
        while a % 10 == 0:
            c+=1
            a //= 10
        return c


        
        