class Solution:
    def possibleBipartition(self, length: int, dislikes: List[List[int]]) -> bool:
        paints = [-1 for _ in range(length)]
        graph = defaultdict(list)
        for i, j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        # print(graph)
        
        def dfs(node, color):
            paints[node] = color
            # print(node, color, paints)
            for neighbor in graph[node]:
                if paints[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif paints[neighbor] == color:
                    return False
            return True
        for i in range (0, length):
            if paints[i] == -1:
                if not dfs(i, 0):
                    return False
        return True



        
                

        