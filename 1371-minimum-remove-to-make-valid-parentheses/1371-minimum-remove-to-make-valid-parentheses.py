class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        brackets = []
        maps = []

        for w in s:
            if w == ")":
                if brackets and brackets[-1] == "(":
                    brackets.pop()
                    maps.pop()
                    stack.append(w)
                # else skip invalid ')'
            elif w == "(":
                maps.append(len(stack))
                brackets.append("(")
                stack.append(w)
            else:
                stack.append(w)

        indexes = set(maps)
        res = []
        for i, ch in enumerate(stack):
            if i not in indexes:
                res.append(ch)

        return "".join(res)
