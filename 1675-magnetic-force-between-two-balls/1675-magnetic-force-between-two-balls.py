class Solution:
    def maxDistance(self, nums: List[int], m: int) -> int:

        def check(k):
            c = 1
            prev = nums[0]
            for i in range(1, len(nums)):
                if prev + k <= nums[i]:
                    prev = nums[i]
                    c+=1
                if c == m:
                    return True
            return False
        nums.sort()
        left = 1
        right = max(nums) - min(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
            


        
        