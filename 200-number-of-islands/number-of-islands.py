class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])


        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col):
 
            visited[row][col] = 1
            dirs = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc
                if(0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1' and visited[new_row][new_col] == 0):
                    dfs(new_row, new_col)
            return 

        for row in range(rows):
            for col in range(cols):
                if(grid[row][col] == '1' and visited[row][col] == 0):
                    dfs(row, col)
                    islands += 1

        return islands