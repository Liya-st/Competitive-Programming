class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        graph = defaultdict(list)
        stack = [0]

        while stack:
            node = stack.pop()
            for n in rooms[node]:
                if not visited[n]:
                    visited[n] = True
                    stack.append(n)
        return all(visited)

        

        
        