class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        thread = []
        prev = 0
        for i, task in enumerate(tasks):
            task.append(i)
        heap = []
        tasks.sort()
        res = []
        heapify(heap)
        i = 0

        while heap or i < len(tasks):
            while i < len(tasks) and prev >= tasks[i][0]:
                start, dur, idx = tasks[i]
                heappush(heap, (dur, idx))
                i+=1
            if heap:
                dur, idx = heappop(heap)
                prev += dur
                res.append(idx)
            else:
                prev = tasks[i][0]
        return res
            
            
            









