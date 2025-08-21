class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        dic = [[[0] for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    dic[i][j] = matrix[i][j]
                else:
                    dic[i][j] = 0 if not matrix[i][j] else (dic[i][j-1] if j > 0 else 0) + 1
                temp = dic[i][j]
                for l in range(i, -1,-1):
                    temp = min(temp, dic[l][j])
                    if not temp:
                        break
                    res += temp
        return res

