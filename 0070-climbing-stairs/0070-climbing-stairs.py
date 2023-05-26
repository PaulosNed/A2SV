class Solution:
    def climbStairs(self, n: int, memo = defaultdict()) -> int:
        if n == 0:
            return 1
        
        if n < 0:
            return 0
        
        if n in memo:
            return memo[n]
        
        way1 = self.climbStairs(n-1)
        way2 = self.climbStairs(n-2)
        
        memo[n] = way1 + way2
        
        return memo[n]
        
        