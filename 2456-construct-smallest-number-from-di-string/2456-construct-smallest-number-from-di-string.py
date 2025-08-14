class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = []
        for i in range(len(pattern)+ 1):
            stack.append(str(i+1))
            while stack and i < len(pattern) and pattern[i] == "I":
                temp = stack.pop()
                res.append(temp)
        while stack:
            temp = stack.pop()
            res.append(temp)
        return "".join(res)
            