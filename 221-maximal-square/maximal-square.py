class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[0] * n for _ in range(m)]
        biggest_square = 0
        for i in range (0, m):
            for j in range (0, n):

                if (matrix[i][j] == "1"):
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        min_squares = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                        dp[i][j] = 1 + min_squares

                    if (dp[i][j] > biggest_square):
                        biggest_square = dp[i][j]
        return biggest_square*biggest_square


    
