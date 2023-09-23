class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        end = len(prices) - 1
        max_idx = end
        max_profit = float("-inf")
        
        while end >= 0:
            if prices[max_idx] > prices[end]:
                max_profit = max(max_profit, prices[max_idx] - prices[end])
            
            else:
                max_idx = end
            
            end -= 1
        
        return max(0, max_profit)