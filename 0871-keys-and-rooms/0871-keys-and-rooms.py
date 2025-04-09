class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        def dfs(node):
            visited.add(node)
            for neigh in rooms[node]:
                if neigh not in visited:
                    dfs(neigh)
        dfs(0)
        return len(rooms) == len(visited)
        

        

        
        