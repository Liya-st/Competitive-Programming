class Solution(object):
    def dailyTemperatures(self, temps):
        """
        :type temps: List[int]
        :rtype: List[int]
        """
        res = [0]*(len(temps))
        stack = []
        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

        