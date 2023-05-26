class Solution(object):
    def fib(self, n, memo = defaultdict()):
        if n == 0 or n == 1:
            return n
        
        if n not in memo:
            memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return memo[n]
