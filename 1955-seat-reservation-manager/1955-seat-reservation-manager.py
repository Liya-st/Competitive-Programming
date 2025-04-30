class SeatManager:

    def __init__(self, n: int):
        self.n = list(range(1, n+1))
        heapify(self.n)
        

    def reserve(self) -> int:
       return heappop(self.n)
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.n, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)