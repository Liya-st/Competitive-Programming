class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = float('inf')

        while left <= right:
            temp = 0
            cap = (left + right) // 2
            i = 0
            day = 1
            for w in weights:
                if temp + w > cap:
                    day +=1
                    temp = 0
                    # continue
                temp += w
            if day <= days:
                res = min(res, cap)
                right = cap -1
            else:
                left = cap + 1
        return res
            
                

