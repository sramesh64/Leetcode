class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(heights)
        columns = len(heights[0])
        pacific = [[False] * columns for _ in range(rows)]
        atlantic = [[False] * columns for _ in range(rows)]

        def dfs(row, column, ocean):
            ocean[row][column] = True

            steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for a, b in steps:
                if(row + a >= 0 and column + b >= 0 and row + a <= rows - 1 and column + b <= columns - 1 and heights[row + a][column + b] >= heights[row][column] and ocean[row + a][column + b] == False):
                    dfs(row + a, column + b, ocean)


        for i in range(columns):
            dfs(0, i, pacific)
            dfs(rows - 1, i, atlantic)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, columns - 1, atlantic)

        result = []
        for row in range(rows):
            for column in range(columns):
                if(pacific[row][column] == atlantic[row][column] == True):
                    result.append([row, column])

        return result
        