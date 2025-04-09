class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        paints= {i : -1 for i in range(numCourses)}
        graph= defaultdict(list)
        cycle = False
        for i, j in prerequisites:
            graph[i].append(j)
        def dfs(node):
            nonlocal cycle
            paints[node] = 0
            if cycle:
                return
            for neigh in graph[node]:
                if paints[neigh] == -1:
                    dfs(neigh)
                elif paints[neigh] == 0:
                    cycle = True
            paints[node] = 1
        for i in range(numCourses):
            if paints[i] == -1:
                dfs(i)
        return not cycle



        