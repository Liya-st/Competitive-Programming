class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        sCount = Counter()
        pCount = Counter(p)
        res = []

        for n in range(len(p)):
            sCount[s[n]] += 1
        
        if pCount == sCount:
            res.append(0)

        for i in range(len(p), len(s)):
            sCount[s[i - len(p)]] -= 1
            if sCount[s[i - len(p)]] == 0:
                del sCount[s[i - len(p)]]
                
            sCount[s[i]] += 1
            
            if pCount == sCount:
                res.append(i - len(p) + 1)

        return res

         
        
        
