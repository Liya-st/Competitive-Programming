class RandomizedSet:

    def __init__(self):
        self.map_index = defaultdict(int)
        self.nums = []
        
    def insert(self, val: int) -> bool:
        if val in self.map_index:
            return False
        self.nums.append(val)
        self.map_index[val] = len(self.nums) -1
        return True

    def remove(self, val: int) -> bool:
        if val in self.map_index:
            idx = self.map_index[val]
            if idx != len(self.nums)-1:
                num = self.nums[-1]
                self.nums[idx] = num
                self.map_index[num] = idx
            self.nums.pop()
            del self.map_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
