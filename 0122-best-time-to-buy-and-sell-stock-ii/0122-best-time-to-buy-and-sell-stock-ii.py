class Solution:
    def maxProfit(self, prices):
        profit  = 0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit