class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def fir(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1  
                else:
                    left = mid + 1
            return first

        def last(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        last = mid
                    left = mid + 1 
                else:
                    right = mid - 1
            return last

        return [fir(nums, target), last(nums, target)]
