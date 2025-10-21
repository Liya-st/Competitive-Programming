class Solution:

    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        self.original = list(nums)    

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        c = len(self.nums)
        while c >= 0:
            idx1 = random.choice(list(range(len(self.nums))))
            idx2 = random.choice(list(range(len(self.nums))))
            self.nums[idx1], self.nums[idx2] = self.nums[idx2], self.nums[idx1]
            c-=1
        return self.nums

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()