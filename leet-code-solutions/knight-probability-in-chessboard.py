class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]
        outOfBound = 0
        
        def isBounded(r, c):
            if 0 <= r < n and 0 <= c < n:
                return True
            
            return False
        
        @cache
        def dp(r, c, power):
            if k == power and isBounded(r, c):
                return 1
            
            if not isBounded(r, c):
                return 0
            
            count = 0
            for mr, mc in directions:
                count += dp(r+mr, c+mc, power+1)
            
            return count
        
        return dp(row, column, 0) / (8 ** k)
    