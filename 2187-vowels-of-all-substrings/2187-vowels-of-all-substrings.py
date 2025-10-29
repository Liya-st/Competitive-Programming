class Solution:
    def countVowels(self, word: str) -> int:
        c = 0
        for i, w in enumerate(word):
            if w in "aeiou":
                c += (i + 1) * (len(word) - i)
        return c 
        