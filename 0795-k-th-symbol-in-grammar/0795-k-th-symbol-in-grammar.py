class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        mid = 2**(n-2)
        if k > mid:
            return 1 - self.kthGrammar(n, abs(k-mid))
        else:
            return self.kthGrammar(n-1, k)

    
        