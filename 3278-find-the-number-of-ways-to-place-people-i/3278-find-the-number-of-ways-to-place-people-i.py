class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0

        for i in range(0, len(points)-1):
            ma = points[i][1]
            mi = -1
            for j in range(i+1, len(points)):
                x, y = points[j]
                if y > ma or y <= mi:
                    continue
                mi = y
                ans += 1
        return ans
