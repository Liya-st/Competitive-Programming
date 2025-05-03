class Solution:
    def equalFrequency(self, word: str) -> bool:
    
        c = Counter(word)
        dic = [v for v in c.values()]
        for i in range(len(dic)):
            dic[i] -= 1
            if len(set(dic)) == 1:
                return True
            if dic[i] == 0:
                if len(set(dic)) == 2:
                    return True
            dic[i] += 1
        return False
        