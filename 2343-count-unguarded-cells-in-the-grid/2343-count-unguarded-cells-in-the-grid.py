class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = [[0] * n for _ in range(m)]
        guardSet = set((x,y) for (x,y) in guards)
        wallSet = set((x,y) for (x,y) in walls)
        
        def dfsGuard(idx, jdx, dir):
            if idx == -1 or idx == m or jdx == -1 or jdx == n or (idx,jdx) in guardSet or (idx,jdx) in wallSet:
                return

            if not guarded[idx][jdx]:
                self.ans -= 1
                guarded[idx][jdx] = 1

            if dir == "west":
                dfsGuard(idx-1, jdx, "west")
            elif dir == "east":
                dfsGuard(idx+1, jdx, "east")
            elif dir == "south":
                dfsGuard(idx, jdx-1, "south")
            else:
                dfsGuard(idx, jdx+1, "north")

        self.ans = m * n 
        for idx in range(m):
            for jdx in range(n):
                if (idx, jdx) in wallSet:
                    self.ans -= 1
                elif (idx, jdx) in guardSet:
                    self.ans -= 1
                    dfsGuard(idx-1, jdx, "west")
                    dfsGuard(idx+1, jdx, "east")
                    dfsGuard(idx, jdx-1, "south")
                    dfsGuard(idx, jdx+1, "north")
        
        return self.ans