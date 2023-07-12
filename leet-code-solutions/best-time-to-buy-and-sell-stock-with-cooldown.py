class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        if len(prices) == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0
        
        sell = [0, max(0, prices[1] - prices[0])]
        buy = [-prices[0], max(-prices[0], -prices[1])]
        
        for i in range(2, len(prices)):
            sell.append(max(sell[i-1], prices[i] + buy[i-1]))
            buy.append(max(buy[i-1], sell[i-2] - prices[i]))
        
        # print(sell, buy)
        
        return sell[-1]