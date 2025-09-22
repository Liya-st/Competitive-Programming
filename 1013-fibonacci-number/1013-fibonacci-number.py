class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def recur(n, memo):
            if n == 0 or n == 1:
                return n
            if n not in memo:
                memo[n] = recur(n-1, memo) + recur(n-2, memo)
            return memo[n] 
        return recur(n, memo)

        