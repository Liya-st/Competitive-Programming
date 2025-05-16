class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c = 0
        while right != left:
            right >>= 1
            left >>= 1
            c += 1
        return left << c

