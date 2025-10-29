class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        safe = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            
            if(not (0 <= i < rows and 0 <= j < cols) or board[i][j] == 'X' or safe[i][j] == 1):
                return

            safe[i][j] = 1

            for di, dj in dirs:
                new_i = i + di
                new_j = j + dj
                
                dfs(new_i, new_j)
            
            

        for i in range(rows):
            for j in [0, cols - 1]:
                if(board[i][j] == 'O'):
                    dfs(i, j)

        for i in range(cols):
            for j in [0, rows - 1]:
                if(board[j][i] == 'O'):
                    dfs(j, i)
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == 'O' and safe[i][j] == 0):
                    board[i][j] = 'X'     