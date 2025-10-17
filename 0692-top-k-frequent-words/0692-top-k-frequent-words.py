class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for x in words:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]