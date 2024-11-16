class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        str_ = ""
        j = 0
        for i in range(len(spaces)):
            str_ += s[j:spaces[i]]
            str_ += " "
            j =spaces[i]
        str_ += s[j:]
        return str_

        
