class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(array, target):
            left, right = 0, len(array) - 1
            while left <= right:
                mid = (right + left) // 2
                if array[mid] < target:
                    left = mid + 1
                elif array[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False 

        num_rows = len(matrix)
        for i in range(num_rows):
            exists = binary_search(matrix[i], target)
            if exists:
                return exists
        return False 