class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, temp):
            if i > n:
                return
            if len(temp) == k:
                res.append(temp[:])
                return
            max_ = n - (k-i) + 1
            for idx in range(i+1, max_+1):
                temp.append(idx)
                helper(idx, temp)
                temp.pop()
             
        helper(0,[])
        return res



        