class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        q = [(0, 0)]  
        
        while q:
            d, node = heapq.heappop(q)
            if d > dist[node]:
                continue
            
            for neigh, w in graph[node]:
                weight = d + w
                
                if weight < dist[neigh]:
                    dist[neigh] = weight
                    ways[neigh] = ways[node]
                    heapq.heappush(q, (weight, neigh))
                
                elif weight == dist[neigh]:
                    ways[neigh] = (ways[neigh] + ways[node]) % MOD
        
        return ways[n - 1] % MOD
