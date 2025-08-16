class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        words = list(s.split())

        #get the longest word
        max_word = max(words, key= len)
        temp = ''

        for i in range(len(max_word)):
            for word in words:
                if i >= len(word):
                    temp += " "
                else:
                    temp += word[i]
            result.append(temp.rstrip())
            temp = ''    
        return result




        
        
        