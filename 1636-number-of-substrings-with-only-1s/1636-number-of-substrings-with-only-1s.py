class Solution:
    def numSub(self, s: str) -> int:
        res, temp = 0, 0
        for i in range(len(s)):
            if s[i] == "0":
                res += temp * (temp + 1) // 2
                temp = 0
            else:
                temp += 1

        res += temp * (temp + 1) // 2
        return res % (10**9 + 7)