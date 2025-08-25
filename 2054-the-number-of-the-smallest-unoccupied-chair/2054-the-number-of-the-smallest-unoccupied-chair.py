class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        heap = list(range(len(times)))
        heapify(heap)
        agg = []
        for idx, (i, j) in enumerate(times):
            agg.append((i, j, idx))
        agg.sort()
        chairs = []
        for i, j, idx in agg:
            while chairs and i >= chairs[0][0]:
                leave, index = heappop(chairs)
                heappush(heap, index)
            x = heappop(heap)
            if idx == targetFriend:
                return x
            heappush(chairs, [j, x])
        return -1
            

            
