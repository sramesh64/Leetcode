class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        biggest_square = 0

        for r in range (rows):
            for c in range (cols):
                if(matrix[r][c] == "0"):
                    dp[r][c] = 0
                else:

                    dp[r][c] = 1 + min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1])
                    
                biggest_square = max(biggest_square, dp[r][c]*dp[r][c])

        return biggest_square