class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calculate(nums):
            if len(nums) <= 2:
                return nums
            arr = []
        
            for i in range(1, len(nums), 2):
                left = calculate(nums[:i])
                right = calculate(nums[i+1:])
                for n in left:
                    for num in right:
                        if nums[i] == '+':
                            arr.append(n + num)
                        elif nums[i] == '-':
                            arr.append(n - num)
                        else:
                            arr.append(n * num)
            return arr
        
        nums = []
        temp = ''
        for n in expression:
            if n.isdigit():
                temp += n
            else:
                nums.append(int(temp))
                nums.append(n)
                temp = ''
        if temp: 
            nums.append(int(temp))
        return calculate(nums)
