class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        outer = len(matrix)-1
        inner = len(matrix[0])-1
        for row in range (outer):
            for col in range (inner):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        return True


