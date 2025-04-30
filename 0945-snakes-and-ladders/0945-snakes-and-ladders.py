class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def coor(num):
            bottom =  ((num - 1) // n)
            r = n - bottom - 1
            c = 0
            if bottom % 2 != 0:
                c = n - 1 - (num - 1) % n
            else:
                c = (num-1) % n
            return (r, c)
        q = deque([(1, 0)])
        visited = [False] * (n * n + 1)
        max_ = 0
        while q: 
            node, rolls = q.popleft()
            if node == n*n:
                return rolls
            visited[node] = True
            max_ = max(rolls, max_)
            for i in range(1, 7):
                square = node + i
                if square > n*n:
                    break
                i, j = coor(square)
                if board[i][j] != -1 and not visited[board[i][j]]:
                    visited[board[i][j]] = True
                    q.append((board[i][j], rolls + 1))
                elif board[i][j] == -1 and not visited[square]:
                    visited[square] = True
                    q.append((square, rolls + 1))

        return -1
            
    
        


            
        