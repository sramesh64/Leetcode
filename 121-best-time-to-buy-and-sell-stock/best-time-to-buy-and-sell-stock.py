class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        dp = [0] * len(prices)
        for i in range (0, len(prices)):
            dp[i] = prices[i] - min_price
            min_price = min(min_price, prices[i])
        return max(dp)
            
    
    def min(self, a, b):
        if (a < b):
            return a
        return b

