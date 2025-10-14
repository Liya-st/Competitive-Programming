class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # keeps track of our char to count ratio
        stack = []

        for letter in s:
            if stack and letter == stack[-1][0]:
                let, count = stack.pop()
                if count != k -1:        
                    stack.append((let, count + 1))
            else:
                stack.append((letter, 1))
        return "".join(ch * cnt for ch, cnt in stack)

        