class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        """
        offset = [(0,1),(0,-1),(-1,0),(1,0)]

        def inbound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0]) 

        def dfs(i,j):
            board[i][j] = 't'
            for row, col in offset:
                new_row = row + i
                new_col = col + j
                if inbound(new_row, new_col) and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][len(board[0])-1] == 'O':
                dfs(i,len(board[0])-1)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[len(board)-1][j] == 'O':
                dfs(len(board)-1,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 't':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
