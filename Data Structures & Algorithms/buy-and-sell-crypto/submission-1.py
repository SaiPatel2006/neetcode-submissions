class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxProfit = 0 #always update this when you find new max
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r+=1
        return maxProfit

        