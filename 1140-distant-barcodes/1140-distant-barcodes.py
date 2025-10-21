class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        heap = []
        for k, v in c.items():
            heap.append((-v, k))
        heapify(heap)
        prev = (0, 0)
        res = []
        while heap:
            c, b = heappop(heap)

            res.append(b)

            if prev[0] < 0:
                heappush(heap, prev)
            
            prev = (c + 1, b)
        return res

                



