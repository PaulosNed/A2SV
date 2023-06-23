class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def isBounded(i, j):
            if i >= len(triangle):
                return True
            
            if 0 <= j < len(triangle[i]):
                return True
            
            return False
        
        @cache
        def dp(i, j):
            if i >= len(triangle):
                return 0
            
            option1 = float('inf')
            option2 = float('inf')
            
            if isBounded(i+1, j):
                option1 = dp(i+1, j)
            if isBounded(i+1, j+1):
                option2 = dp(i+1, j+1)
            
            return min(option1, option2) + triangle[i][j]
        
        return dp(0,0)
        