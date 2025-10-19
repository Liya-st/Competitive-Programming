class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        arr = []
        i = 0
        for k, v in count.items():
            arr.append(-v )
        
        heapq.heapify(arr)
        res = 0
        q = deque()
        while arr or q:
            res +=1
            if arr:
                c = 1 + heappop(arr)
                if c < 0:
                    q.append((c, res + n))
            while q and q[0][1] <= res:
                temp, _ = q.popleft()
                heappush(arr, temp)
        return res
            
                



