class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        nums[:] = red * [0] + white * [1] + blue * [2]
            

        
