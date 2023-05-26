class Solution(object):
    def fib(self, n, memo = defaultdict()):
        if (n == 1):
            return 1
        
        if (n == 0):
            return 0
        
        if n in memo:
            return memo[n]
        
        prev1 = self.fib(n-1, memo)
        prev2 = self.fib(n-2, memo)
        
        memo[n] = prev1 + prev2
        
        return memo[n]
