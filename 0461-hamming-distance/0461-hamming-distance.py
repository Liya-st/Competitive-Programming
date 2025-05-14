class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        return n.bit_count()
        