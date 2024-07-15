class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        c_str = ""
        n = 0

        for c in s:
            if c.isdigit():
                n = n*10 + int(c)
            elif c=='[':
                stack.append(n)
                stack.append(c_str)
                n = 0
                c_str=""
            elif c==']':
                prev_s = stack.pop()
                prev_n = stack.pop()
                c_str = prev_s + c_str*prev_n
            else:
                c_str +=c
        return c_str