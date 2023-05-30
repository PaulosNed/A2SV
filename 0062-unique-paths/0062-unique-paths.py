class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1, 0), (0, 1)]
        
        def dp(curr, memo):
            if curr == (m-1, n-1):
                return 1
            
            if curr in memo:
                return memo[curr]
            
            for direction in directions:
                nxt = (curr[0] + direction[0], curr[1] + direction[1])
                if isBounded(nxt):
                    memo[curr] += dp(nxt, memo)
            
            return memo[curr]
        
        def isBounded(curr):
            return 0 <= curr[0] < m and 0 <= curr[1] < n
        
        memo = defaultdict(int)
        return dp((0,0), memo)
            