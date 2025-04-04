class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        res = 0
        MOD = (10 ** 9)+ 7
        
        for n in instructions:
            idx = nums.bisect_right(n)
            i = nums.bisect_left( n)
            res = (res + min(len(nums)-idx, i)) % MOD
            nums.add(n)
        return res % MOD