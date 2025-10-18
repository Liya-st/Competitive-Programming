class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        max_ = 0
        res = 0
    
        for r in range(len(s)):
            count[s[r]] +=1
            max_ =  max(count.values())

            length = r - l + 1
            while r > l and r-l + 1 - max_ > k:
                count[s[l]] -=1
                l +=1
            res = max(res, r - l + 1)
        return res
            

            
        