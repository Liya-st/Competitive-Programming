class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def f(i, mod):
            if i<0: return 0 if mod==0 else -(1<<30)
            num = nums[i]
            prev = (mod-num ) % 3
            if prev<0:prev+=3
            return max (num + f(i-1, prev), f(i-1, mod))
        return max(0, f(n-1, 0))