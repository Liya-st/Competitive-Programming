class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        for n in range(len(piles)//3 , len(piles), 2):
            res += piles[n]
        return res


        
        
