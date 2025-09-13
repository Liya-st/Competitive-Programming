class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = Counter(s)
        vowel = max((dic[ch] for ch in dic if ch in "aeiou"), default=0)
        consonant = max((dic[ch] for ch in dic if ch not in "aeiou"), default=0)
        return vowel + consonant