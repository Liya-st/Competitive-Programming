class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(start,temp):
            if len(temp)==len(s):
                res.append(temp[:])
                return

            for i in range(start,len(s)):
                if s[i].isdigit():
                    backtrack(i+1,temp+s[i])
                else:
                    low = temp+s[i].lower()
                    backtrack(i+1,low)
                    up = temp+s[i].upper()
                    backtrack(i+1,up)
        res = []
        backtrack(0,"")
        return res