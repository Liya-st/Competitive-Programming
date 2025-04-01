class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open, closed, limit, s):
            if open == limit and closed == limit:
                res.append("".join(s))
                s = ''
                return
            if open < limit: 
                s.append('(')
                backtrack(open + 1, closed, limit,s )
                s.pop()
            if open > closed:
                s.append(')')
                backtrack(open, closed + 1, limit, s)
                s.pop()
        backtrack(0, 0, n, [])
        return res
            
            

        