class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(zero, n, s):
            if len(s) == n:
                res.append("".join(s))
                return
            if zero:
                s.append("1")
                backtrack(False, n, s)
                s.pop()
            else:
                s.append("0")
                backtrack(True, n, s)
                s.pop()
                s.append("1")
                backtrack(False, n, s)
                s.pop()
        backtrack(False, n, [])
        return res

        