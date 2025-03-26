class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_ = min(ranks)
        max_ = max(ranks)
        right = min_ * (cars * cars)
        left = 0
        res = -1
        

        while left <= right:
            mid = (left + right) // 2
            sum_ = 0
            for n in ranks:
                sum_ += int((mid//n)**0.5)
            if sum_ >= cars:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        


        