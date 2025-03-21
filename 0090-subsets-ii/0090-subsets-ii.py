class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        subsets.add(())
        temp = []
        nums.sort()
        def backtrack(i, temp):
            if i >= len(nums):
                return

            for idx in range(i, len(nums)):
                if idx > i and nums[idx] == nums[idx - 1]:
                    continue

                temp.append(nums[idx])
                subsets.add(tuple(temp))
                backtrack(idx+1, temp)
                temp.pop()
        backtrack(0, temp)
        return list(subsets)