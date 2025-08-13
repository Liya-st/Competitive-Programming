class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = num2.bit_count()
        res = 0
        for i in range(32, -1, -1):
            if set_bits == 0:
                break
            if 1 & (num1 >> i):
                res |= 1 << i
                set_bits -=1
        i = 0
        while set_bits > 0:
            if (res >> i)& 1 == 0:
                res |= 1 << i
                set_bits -=1
            i+=1
        return res

            
        
