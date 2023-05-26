class Solution(object):
    def fib(self, n, memo = defaultdict()):
        if (n == 1):
            return 1
        
        elif(n == 0):
            return 0
        
        prev1 = self.fib(n-1, memo)
        prev2 = self.fib(n-2, memo)
        
        ans = prev1 + prev2
        memo[n] = ans
        
        return ans
