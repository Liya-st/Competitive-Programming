class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        memo = {}
        def dp(idx):
            if idx < 0 or idx >= len(energy):
                return 0 
            
            if idx not in memo:
                memo[idx] = dp(idx + k) + energy[idx]
            return memo[idx]
        res = float("-inf")
        for i in range(len(energy)):
            res = max(res, dp(i))
        return res
        