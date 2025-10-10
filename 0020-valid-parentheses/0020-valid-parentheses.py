class Solution:
    def isValid(self, s: str) -> bool:
        open_closure_map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for token in s:
            if token in open_closure_map:
                stack.append(token)
            else:
                if not stack or open_closure_map[stack.pop()] != token:
                    return False
        return len(stack) == 0