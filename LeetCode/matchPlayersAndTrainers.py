class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i=0;j=0
        c=0
        p=sorted(players,reverse=True)
        t=sorted(trainers,reverse=True)
        while i<len(players) and j<len(trainers):
            if p[i]<=t[j]:
                c+=1
                i+=1
                j+=1
            else:
                i+=1
        return c
            

        
