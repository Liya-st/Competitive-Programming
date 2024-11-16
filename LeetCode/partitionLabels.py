class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}
        res = []
        size,end = 0,0

        for i,c in enumerate(s):
            lastI[c] = i
        
        for i,c in enumerate(s):
            size += 1
            end = max(end, lastI[c])
            if end == i:
                res.append(size)
                size = 0
        return res

        
