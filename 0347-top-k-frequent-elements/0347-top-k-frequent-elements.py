class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        res = []

        for key, v in count.items():
            bucket[v].append(key)
        # print(bucket)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                
                res.append(num)
                if len(res) == k:
                    return res
            
