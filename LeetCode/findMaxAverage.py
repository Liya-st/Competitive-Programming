class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ =  sum1 = sum(nums[:k])
        for i in range(k, len(nums)):
            sum1 += nums[i]
            sum1 -= nums[i-k]

            max_ = max(max_, sum1)
        return max_/k
        
