"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        res = 0
        for n in employees:
            graph[n.id] = [n.importance, n.subordinates]
        def dfs(node):
            x = graph[node]
            total = x[0]
            for n in x[1]:
                total +=  dfs(n)
            return total
        return dfs(id)
            