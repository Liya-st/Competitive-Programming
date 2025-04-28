class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = SortedList(piles)
        sum_ = sum(nums)
        while k > 0:
            x = nums[-1]
            nums.remove(x)
            nums.add(x -  (x // 2)) 
            sum_ -= x // 2
            k -=1
        return sum_

        
        