class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        count = Counter(words[0])
        for word in words:
            curr_count = Counter(word)
            for c in count:
                count[c] = min(count[c], curr_count[c])
            
        for c in count:
            for i in range(count[c]):
                res.append(c)
        return res 

       

            
        
