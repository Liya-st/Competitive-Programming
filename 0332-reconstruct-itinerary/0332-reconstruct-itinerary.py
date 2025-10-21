class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)
        
        route = []
        stack = ["JFK"]
        visited = defaultdict(bool)
        while stack:
            node = stack[-1]
            if graph[node]:
                neigh = graph[node].pop()
                stack.append(neigh)
            else:
                stack.pop()
                route.append(node)
        return route[::-1]
        




        