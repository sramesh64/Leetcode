class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = triangle[-1][:]
        num_rows = len(triangle) - 1
        for i in range (num_rows - 1, -1, -1):
            new_list = [0] * (i+1)
            for j in range(0, len(new_list)):
                new_list[j] = triangle[i][j] + self.min(dp[j], dp[j+1])

            dp = new_list
        
        return dp[0]



    def min(self, a, b):
        if (a < b): 
            return a
        return b
