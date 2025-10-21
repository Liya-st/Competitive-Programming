class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        j = 0
        sum_ = 0
        min_ = inf
        for j in range(len(nums)):
            sum_ += nums[j]
            while sum_ >= target:
                window = j-i+1
                min_ = min(min_, window)
                sum_ -= nums[i]
                i+=1
        return min_ if min_ != inf else 0
                    

        