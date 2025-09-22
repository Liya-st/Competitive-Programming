class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_ = 0
        res = 0
        for n in nums:
            if c[n] > max_:
                res = 0
                max_ = c[n]
            if c[n] == max_:
                res +=1
        return res

        