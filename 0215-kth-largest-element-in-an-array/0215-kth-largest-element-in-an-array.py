class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums) - k
        heapq.heapify(nums)
        while n > 0:
            heapq.heappop(nums)
            n-=1
        return heapq.heappop(nums)
        