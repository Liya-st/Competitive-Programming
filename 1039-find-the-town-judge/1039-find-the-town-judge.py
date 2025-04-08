class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = set()
        res = 0
        num = defaultdict(int)

        for i, j in trust:
            trusts.add(i)
            num[j] +=1

        for i in range(1, n+1):
            if i not in trusts and num[i] == n -1:
                return i
        return -1
        

        