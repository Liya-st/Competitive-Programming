class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp =[]
        col_set = set()
        diag = set()
        d = set()

        def check(i, j):
            if j in col_set:
                return False
            elif i + j in diag or i - j in d:
                return False
            return True
        def backtrack(i):
            if i >= n:
                res.append(temp[:])
                return 
            for k in range(n):
                if check(i, k):
                    temp.append("."* (k) + "Q" + "."*(n-k-1))
                    col_set.add(k)
                    diag.add(i+k)
                    d.add(i-k)
                    backtrack(i+1)
                    temp.pop()
                    col_set.remove(k)
                    diag.remove(i+k)
                    d.remove(i-k)

        backtrack(0)
        return res
        


                
                

            