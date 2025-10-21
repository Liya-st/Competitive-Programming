class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1 and target > k:
            return 0
        memo = defaultdict(int)
        MOD = (10 ** 9 )+ 7

        def dp(rem, sum):
            if rem == 0 and sum == 0:
                return 1
            elif rem == 0 or sum <= 0:
                return 0
            state = (rem, sum)

            if state not in memo:
                memo[state] = 0
                for i in range(1, k+1):
                    temp = rem - 1
                    if temp >= 0 and  sum - i >= 0:
                        memo[state] = (memo[state] + dp(temp, sum - i)) % MOD
            return memo[state]
        return dp(n, target)

        