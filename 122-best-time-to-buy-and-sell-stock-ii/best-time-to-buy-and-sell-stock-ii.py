class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if(prices[i] > min):
                profit += prices[i] - min
            min = prices[i]
        
        return profit

