class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_xor = 0
        range_xor = 0
        for i, n in enumerate(nums):
            arr_xor ^= n
            range_xor ^= i + 1
        return arr_xor ^ range_xor

        