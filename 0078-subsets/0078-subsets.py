class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        temp = set()
        def backtrack(i, temp):
            if i >= len(nums):
                return

            for idx in range(i, len(nums)):
                temp.add(nums[idx])
                subsets.append(list(temp))
                backtrack(idx+1, temp)
                temp.discard(nums[idx])
        backtrack(0, temp)
        return subsets

        