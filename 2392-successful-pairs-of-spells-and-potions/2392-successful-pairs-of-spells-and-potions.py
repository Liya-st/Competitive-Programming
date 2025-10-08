class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        size = len(potions)
        res= []
        for n in  spells:
            pair = (success + n - 1 )// n
            idx = bisect_left(potions, pair)
            res.append(size - idx)
        return res


        