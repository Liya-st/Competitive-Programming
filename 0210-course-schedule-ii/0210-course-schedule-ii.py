class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        x = defaultdict(int)
        res = []
        for u, v in pre:
            graph[v].append(u)
            x[u] += 1
        start = deque()
        vis = set()
        for i in range(num):
            if i not in x:
                start.append(i)
        while start:
            node = start.popleft()
            if node not in vis:
                res.append(node)
            vis.add(node)
            for neigh in graph[node]:
                x[neigh] -=1
                if neigh not in vis and x[neigh] == 0:
                    start.append(neigh)
        if len(res) == num:
            return res           
        return []

        