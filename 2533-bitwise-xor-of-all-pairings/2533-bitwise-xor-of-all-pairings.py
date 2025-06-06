class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0
        xor2 = 0
        for n in nums1:
            xor ^= n
        for n in nums2:
            xor2 ^= n

        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        elif len(nums1) % 2 != 0 and len(nums2) % 2 == 0:
            return xor2
        elif len(nums1) % 2 == 0 and len(nums2) % 2 != 0:
            return xor
        
        return xor ^ xor2
