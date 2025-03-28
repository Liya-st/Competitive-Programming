import bisect
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        left, right = 0, max(max(houses), max(heaters))
        
        def check(k):
            for house in houses:
                j = bisect.bisect_left(heaters, house) 

                if j < len(heaters) and abs(heaters[j] - house) <= k:
                    continue
                if j > 0 and abs(heaters[j - 1] - house) <= k:
                    continue
                
                return False  
            
            return True  
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
