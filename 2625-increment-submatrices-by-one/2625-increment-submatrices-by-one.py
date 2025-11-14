class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        for sx, sy, ex, ey in queries:
            for i in range(sx, ex + 1):
                mat[i][sy] += 1
                if ey + 1 < n:
                    mat[i][ey + 1] -= 1

        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        return mat
