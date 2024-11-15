class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = [str(num) for num in nums]
        n.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        if n[0] == '0':
            return "0"
        res = ''.join(n)
        return res
        
