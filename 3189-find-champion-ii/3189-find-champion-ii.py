class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [0]*n
        for u, v in edges:
            graph[v] +=1
        c = []
        

        for i in range(n):
            if graph[i] == 0:
                c.append(i)
        if len(c) == 1:
            return c[0]
        else:
            return -1


        
            


        
        