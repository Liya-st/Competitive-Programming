class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for n in s:
            if n == ')':
                x = stack.pop()
                if x == 0:
                    stack.append(1)
         
                else:
                    sum_ = x
                    while stack and stack[-1] != 0:
                        sum_ += stack.pop()
                    if stack: 
                        sum_ += stack.pop()   
                    stack.append(sum_*2)       
            else:
                stack.append(0)
        return sum(stack)

        