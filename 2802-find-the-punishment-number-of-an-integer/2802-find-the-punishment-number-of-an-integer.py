class Solution:
    def punishmentNumber(self, n: int) -> int:  
        def backtrack(curr, idx, n, s):
            if curr > n:
                return False
            if idx == len(s):
                return curr == n

            for i in range(idx, len(s)):
                temp = int(s[idx:i+1])
                if backtrack(curr + temp, i+1, n, s):
                    return True
            return False
        sum_= 0
        for num in range(1, n+1):
            if backtrack(0, 0, num, str(num*num)):
                sum_ += num*num
        return sum_
            


