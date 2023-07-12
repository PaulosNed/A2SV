class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        sell = [0]
        buy = [-prices[0]-fee]
        
        for i in range(1, len(prices)):
            sell.append(max(sell[i-1], prices[i] + buy[i-1]))
            buy.append(max(buy[i-1], sell[i-1] - prices[i] - fee))
        
        return sell[-1]