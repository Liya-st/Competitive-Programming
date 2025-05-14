class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * (len(arr) + 1)
        acc = 0
        res= []
        for i, n in enumerate(arr):
            acc ^= n
            prefix_xor[i+1] = acc
        for i, j in queries:
            res.append(prefix_xor[j+1] ^ prefix_xor[i])
        return res