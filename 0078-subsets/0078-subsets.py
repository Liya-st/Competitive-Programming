class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # take or no take approach
        subsets = []
        temp = []
        def backtrack(i, temp):
            if i >= len(nums):
                subsets.append(temp[:])
                return

            temp.append(nums[i])
            backtrack(i+1, temp)
            temp.pop()
            backtrack(i+1, temp)
        backtrack(0, temp)
        return subsets

        