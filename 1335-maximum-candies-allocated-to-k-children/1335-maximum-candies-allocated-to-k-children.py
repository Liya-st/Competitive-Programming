class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            count = 0
            for candy in candies:
                count += candy // mid
                if k <= count:
                    return True
            return False

        if sum(candies) < k:
            return 0
        left = 1
        right = sum(candies) // k
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
            
        