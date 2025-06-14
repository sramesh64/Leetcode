class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0): return 0
        if (n == 1): return 1
        L = [0] * n
        L[0] = 1
        L[1] = 2


        for i in range(2, n):
                L[i] = L[i-1] + L[i-2]

        return L[n-1]

