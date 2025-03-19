class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, temp):
            if len(temp) == k:
                res.append(temp[:])
                return
            if i > n:
                return

            temp.append(i)
            backtrack(i+1, temp)
            temp.pop()
            backtrack(i+1, temp)
        backtrack(1, [])
        return res
       



        