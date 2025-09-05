class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num2 >= num1:
            return -1
        for i in range(1, 61):
            temp = num1 - i*num2 
            if temp >= 0 and temp.bit_count() <= i <= temp:
                return i
        return -1

        

            
                    




        
        