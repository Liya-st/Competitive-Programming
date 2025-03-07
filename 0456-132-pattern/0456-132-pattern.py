class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        x = float('-inf')

        for n in reversed(nums):
            if n < x:
                return True
            while stack and stack[-1] < n:
                x = stack.pop()
            stack.append(n)
        return False

