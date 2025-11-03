class Solution(object):
    def minCost(self, colors, neededTime):
        n, sum_ = len(colors), 0
        i = 1
        while i < n:
            max_ = 0
            while i < n and colors[i] == colors[i - 1]:
                sum_ += neededTime[i - 1]
                max_ = max(max_, neededTime[i - 1])
                i += 1
            sum_ += neededTime[i - 1]
            max_ = max(max_, neededTime[i - 1])
            if max_ != 0:
                sum_ -= max_
            i += 1
        return sum_