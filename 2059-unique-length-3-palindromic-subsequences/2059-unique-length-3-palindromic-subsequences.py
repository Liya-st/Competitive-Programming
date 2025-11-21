class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pre = [-1] * 26
        post = [-1]*26
        res = 0

        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if pre[idx] == -1:
                pre[idx] = i

            post[idx] = i

        for i in range(26):
            sub = set()
            if pre[i] != -1:
                for n in range(pre[i] + 1, post[i]):
                    sub.add(s[n])
                res += len(sub)

        return res
            
