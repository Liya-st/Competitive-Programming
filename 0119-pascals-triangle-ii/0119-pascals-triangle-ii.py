class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        prev = self.getRow(rowIndex-1)
        tri = [1]*(rowIndex + 1)
        for i in range(1, rowIndex):
            tri[i] = prev[i-1]+prev[i]
        return tri


        