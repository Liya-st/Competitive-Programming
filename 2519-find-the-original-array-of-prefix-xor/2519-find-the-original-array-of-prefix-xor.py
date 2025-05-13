class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        temp = 0
        res= [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i-1]^pref[i])
        return res
        