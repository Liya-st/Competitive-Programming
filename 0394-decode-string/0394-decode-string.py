class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []
        for w in s:
            if w.isalnum() or w == '[':
                stack.append(w)
            else:
                num = ""
                temp = ""
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                st = temp * int(num)
                stack.extend(list(st))
        return "".join(stack)

                    
                        
