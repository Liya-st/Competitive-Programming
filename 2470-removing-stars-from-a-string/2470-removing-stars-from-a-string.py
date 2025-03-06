class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in range(len(s)):
            if s[i] == '*':
                res.pop()
            else:
                res.append(s[i])
        return "".join(res)
    



        