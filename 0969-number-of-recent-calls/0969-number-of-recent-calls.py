class RecentCounter(object):

    def __init__(self):
        self.i = 0
        self.calls = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.calls.append(t)
        # print(self.calls)
        while self.calls[self.i] < t - 3000:
            self.i+=1
        return len(self.calls) - self.i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)