class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(i, temp):
            if i >= len(s):
                res.append(temp[:])

            for idx in range(i, len(s)):
                if is_palindrome(s[i:idx+1]):
                    temp.append(s[i:idx+1])
                    backtrack(idx+1,temp)
                    temp.pop()
        def is_palindrome(n):
            if len(n) == 1:
                return True
            l = 0
            j = len(n)-1
            while l < j:
                if n[l] != n[j]:
                    return False
                l+=1
                j-=1
            return True
        backtrack(0, [])    
        return res 
        