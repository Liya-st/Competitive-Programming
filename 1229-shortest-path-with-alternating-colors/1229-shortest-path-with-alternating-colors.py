class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, 1))

        for u, v in blueEdges:
            graph[u].append((v, 0))

        res = [-1]*n
        vis = set()
        q = deque()
        depth = 1
        res[0] = 0
        q.append((0, 0,1)) 
        q.append((0, 1,1))

        while q:
            node, col, depth = q.popleft()
            for neigh, c in graph[node]:
                if col != c and (neigh, c) not in vis:  
                    vis.add((neigh, c))
                    q.append((neigh, c, depth + 1))
                    res[neigh] = depth if res[neigh] == -1 else res[neigh]
        return res


            

