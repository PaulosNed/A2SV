class Solution:
    def __init__(self):
        self.set = set()
        
    def distinctPrimeFactors(self, nums):
        product = 1
        for num in nums:
            self.checker(num)
        
        return len(self.set)
        
    def checker(self, n):
        d = 2
        while(d * d <= n):
            while(n % d == 0):
                self.set.add(d)
                n = n // d
            d += 1
        if n > 1:
            self.set.add(n)

        return