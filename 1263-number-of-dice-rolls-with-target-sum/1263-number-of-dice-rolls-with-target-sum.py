class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1 and target > k:
            return 0
        memo = defaultdict(int)
        MOD = (10 ** 9 )+ 7
        memo = [[0]*(target+1) for _ in range(n + 1)]

        for i in range(n+1):
            for j in range(target + 1):
                if i == 0 and j == 0:
                    memo[i][j] = 1
                elif i == 0 or j == 0:
                    memo[i][j] = 0

        for i in range(1, n+1):
            for j in range(1, target + 1):
                for d in range(1, k + 1):
                    if j - d >= 0:
                        memo[i][j] = (memo[i][j] + memo[i-1][j-d]) % MOD
        return memo[n][target]

        

        

        