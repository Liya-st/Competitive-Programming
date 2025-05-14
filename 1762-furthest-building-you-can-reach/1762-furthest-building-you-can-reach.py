class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            h = heights[i+ 1] - heights[i]
            if h > 0:
                bricks -= h
                heappush(heap, -h)
                if bricks < 0:
                    bricks += -heappop(heap)
                    ladders -=1
                if ladders < 0:
                    return i
        return len(heights) - 1

        