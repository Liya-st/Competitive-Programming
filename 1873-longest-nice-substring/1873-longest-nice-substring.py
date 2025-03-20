class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        dic = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in dic:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s1 if len(s1) >= len(s2) else s2
        return s
            