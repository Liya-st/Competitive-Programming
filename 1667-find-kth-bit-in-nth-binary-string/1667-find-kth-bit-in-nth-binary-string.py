class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = self.binary(n)
        return res[k-1]

    def binary(self, n):
        if n == 1:
            return "0"  
        
        prev = self.binary(n - 1)  
        return prev + "1" + self.flip(prev)[::-1]  

    def flip(self, s):
        st = []
        for n in s:
            if n == "0":
                st.append("1")
            else:
                st.append("0")
        return "".join(st)
    
        