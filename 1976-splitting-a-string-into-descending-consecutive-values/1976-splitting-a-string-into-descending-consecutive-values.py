class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(idx, prev):
            if idx >= len(s):
                return True

            for i in range(idx, len(s)):
                temp = int(s[idx:i+1])
                if temp == prev -1 and backtrack(i+1, temp):
                    return True
            return False
        for i in range(len(s)-1):
            temp = int(s[:i+1])
            if backtrack(i+1, temp):
                return True
        return False
        



        