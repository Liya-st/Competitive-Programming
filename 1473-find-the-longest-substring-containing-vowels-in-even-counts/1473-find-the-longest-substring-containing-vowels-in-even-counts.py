class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        char_map = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        maps = [-1] * 32
        maps[0] = 0  
        res = 0
        acc = 0

        for i in range(len(s)):
            if s[i] in char_map:  
                acc ^= char_map[s[i]]
            if maps[acc] == -1 and acc != 0:
                maps[acc] = i + 1  
            res = max(res, i + 1 - maps[acc])

        return res
