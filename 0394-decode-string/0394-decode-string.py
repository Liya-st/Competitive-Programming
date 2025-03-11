class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = []
        res = []
        for n in s:
            if n == ']':
                while stack and stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                num = "".join(num)
                temp.reverse()
                stack.extend(temp * int(num)) 
                temp = []
            else:
                stack.append(n)
        return "".join(stack)
            
        
            
                    
