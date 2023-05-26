class Solution:
    def climbStairs(self, n: int, memo = defaultdict()) -> int:
        if n <= 2:
            return n
        
        if n not in memo:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return memo[n]
        
        