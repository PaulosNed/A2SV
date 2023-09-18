class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        def isBound(r, c):
            if 0 <= r < len(dungeon) and 0 <= c < len(dungeon[0]):
                return True
            
            return False
        
        @cache
        def dp(r, c):
            if r == len(dungeon) - 1 and c == len(dungeon[0]) - 1:
                return -dungeon[r][c]
            
            ans = float('inf')
            if isBound(r+1, c):
                ans = min(ans, dp(r+1, c))
                
            if isBound(r, c+1):
                ans = min(ans, dp(r, c+1))
                
            if dungeon[r][c] < 0 and ans < 0:
                return -dungeon[r][c]
            
            return ans - dungeon[r][c]
        
        return max(1, dp(0, 0) + 1)