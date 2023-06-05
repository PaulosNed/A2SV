class Solution:
    def tribonacci(self, n: int, memo = defaultdict(int)) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        if n not in memo:
            param1 = self.tribonacci(n-1) 
            param2 = self.tribonacci(n-2) 
            param3 = self.tribonacci(n-3)
            memo[n] = param1 + param2 + param3
        
        return memo[n]