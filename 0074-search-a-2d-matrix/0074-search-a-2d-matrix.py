class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix):
            if matrix[row][col] > target:
                if col - 1 >= 0:
                    col -=1
                else:
                    return False
            elif matrix[row][col] < target:
                if row +1 < len(matrix):
                    row +=1
                else:
                    return False
            else:
                return True
        return False

            
        