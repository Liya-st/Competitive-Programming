class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for (x, y) in points:
            s = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (s, x, y))
            else:
                heapq.heappush(heap, (s, x, y))
        for (s,x, y) in heap:
            res.append((x,y))

        return res