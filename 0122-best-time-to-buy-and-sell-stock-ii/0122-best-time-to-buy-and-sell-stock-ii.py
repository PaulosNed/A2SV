class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buys = [-prices[0]]
        sells = [0]
        
        for i in range(len(prices)):
            buys.append(max(buys[-1], sells[-1] - prices[i]))
            sells.append(max(sells[-1], buys[-1] + prices[i]))
        
        return sells[-1]