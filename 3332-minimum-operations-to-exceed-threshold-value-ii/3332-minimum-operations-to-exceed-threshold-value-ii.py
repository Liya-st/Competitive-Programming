class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            n = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, n)
            c+=1
        return c
        
        