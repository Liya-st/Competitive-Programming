class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        for n in s:
            if n in "aeiou":
                count +=1
        if count == 0:
            return False
        return True
        