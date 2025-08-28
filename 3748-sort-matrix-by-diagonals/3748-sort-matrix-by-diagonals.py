class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        bl = []
        tr = [[]]

        bls = (0,0)
        trs = (0,1)

        for i in range(trs[1], n):
            temp = []
            x, y = (0, i)
            while y < n:
                temp.append(grid[x][y])
                x += 1
                y += 1
            tr.append(temp)
        
        for i in range(bls[0], n):
            temp = []
            x, y = (i, 0)
            while x < n:
                temp.append(grid[x][y])
                x += 1
                y += 1
            bl.append(temp)
        
        for dia in bl:
            dia.sort(reverse=True)
        for dia in tr:
            dia.sort()
        
        g = [[-1 for _ in range(n)] for _ in range(n)]
        print(bl)
        print(tr)

        for i in range(len(bl)):
            x = i
            for j in range(len(bl[i])):
                y = j
                g[x][y] = bl[i][j]
                x += 1
                y += 1
        
        for i in range(1, len(tr)):
            y = i
            for j in range(len(tr[i])):
                x = j
                g[x][y] = tr[i][j]
                y += 1
             
        return (g)
