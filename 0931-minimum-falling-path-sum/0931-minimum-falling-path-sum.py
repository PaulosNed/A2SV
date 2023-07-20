class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        @cache
        def dp(row, col):
            
            if row >= len(matrix):
                return 0
            
            if not 0 <= col < len(matrix[0]):
                return float('inf')
            
            opt1 = dp(row+1, col-1)
            opt2 = dp(row+1, col)
            opt3 = dp(row+1, col+1)
            
            return matrix[row][col] + min(opt1, opt2, opt3)
        
        ans = float('inf') 
        for j in range(len(matrix[0])):
            ans = min(ans, dp(0, j))
        
        return ans
        
        