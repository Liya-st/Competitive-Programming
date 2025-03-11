class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        else:
            return False