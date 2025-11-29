class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_ = sum(nums)
        return sum_ % k 
        