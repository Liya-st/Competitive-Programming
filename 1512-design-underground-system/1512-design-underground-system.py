class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(int)
        self.time = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, time = self.check_in[id]
        total, count = self.time[(name, stationName)] if self.time[(name, stationName)] else [0, 0]
        self.time[(name, stationName)] = [total + (t- time), count +1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.time[(startStation, endStation)] if self.time[(startStation, endStation)] else [0, 0]

        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)