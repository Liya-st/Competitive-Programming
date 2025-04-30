class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for i, row in enumerate(grid):
            row.sort()
            j = len(row)-1
            while limits[i] > 0:
                heappush(heap, row[j])
                j-=1
                limits[i] -=1
            while len(heap) > k:
                heappop(heap)
        return sum(heap)





        