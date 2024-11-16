class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        i, j = 0, len(skill)-1
        sum_ = skill[0] + skill[-1]
        while i < j:
            if skill[i] + skill[j] != sum_:
                return -1
            res += skill[i]*skill[j]
            i+=1
            j-=1
        return res




        
