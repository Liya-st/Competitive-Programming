class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        dic = defaultdict(list)
        for i, row in enumerate(grid):
            dic[i] = [-n for n in row]
            heapify(dic[i])
        temp = []

        for i, n in enumerate(limits):
            while n > 0:
                temp.append(heappop(dic[i]))
                n-=1
      
        heapify(temp)
        sum_ = 0
        while k > 0:
            sum_ += -(heappop(temp))
            k-=1
        return sum_



        