class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        :type operations: List[str]
        :rtype: int
        """
        num = 0
        for op in operations:
            if op[1] == '-':
                num -= 1
            else:
                num += 1
        return num