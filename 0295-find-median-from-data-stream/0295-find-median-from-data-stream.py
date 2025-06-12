class MedianFinder:
    def __init__(self):
        self.s = []  
        self.l = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -num)
        heapq.heappush(self.l, -heapq.heappop(self.s))
        if len(self.l) > len(self.s):
            heapq.heappush(self.s, -heapq.heappop(self.l))

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -self.s[0]
        return (-self.s[0] + self.l[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()