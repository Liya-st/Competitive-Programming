class MinStack:

    def __init__(self):
        self.min_ = inf
        self.stack = []

    def push(self, val: int) -> None:
        self.min_ = min(self.min_, val)
        self.stack.append((val, self.min_))

    def pop(self) -> None:
        self.stack.pop()
        self.min_ = self.stack[-1][1] if self.stack else inf

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()