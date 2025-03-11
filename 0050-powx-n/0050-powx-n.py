class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n     
        res = self.power(n,x)
        return res
    def power(self, n, x):
        if n == 0:
            return 1
        m = self.power(n//2, x)
        if n%2 == 0:
            return m*m
        else:
            return m*m*x

        
        

        