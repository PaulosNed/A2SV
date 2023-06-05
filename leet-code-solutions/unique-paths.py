class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def isBounded(r, c):
            if 0 <= r < m and 0 <= c < n:
                return dp[r][c]
            return 0
            
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[-1][-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] += isBounded(i + 1, j)
                dp[i][j] += isBounded(i, j + 1)
        
        return dp[0][0]
                