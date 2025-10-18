class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                k-=1
                stack.pop()
            if not stack and n == "0":
                continue
            stack.append(n)
        res = stack[:len(stack)-k]
        return "".join(res) if res else "0"
        