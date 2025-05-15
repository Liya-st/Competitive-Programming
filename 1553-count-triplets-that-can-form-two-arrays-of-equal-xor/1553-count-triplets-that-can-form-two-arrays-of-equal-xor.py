class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        acc= 0
        prefix = []
        for n in arr:
            acc ^= n
            prefix.append(acc)
        for i in range(len(arr)):
            acc = 0
            for j in range(i, len(arr)):
                acc ^= arr[j]
                if acc == 0:
                    res += j - i 
        return res
            

    




        